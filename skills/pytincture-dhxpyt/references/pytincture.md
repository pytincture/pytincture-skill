# pytincture quick reference (service mode)

Targets pytincture **1.0.0rc5**. Requires Python 3.13 or 3.14.

## What it is

A Python framework that runs Python-driven UIs in the browser via Pyodide.
Service mode adds a backend: BFF calls, authentication, private server Python,
and backend-hosted widget wheels. Standalone mode has none of that — see
[`pytincture-runtime.md`](pytincture-runtime.md).

## Application layout

```text
my_service/
├── service.py          # ASGI process code; never sent to the browser
├── dashboard.py        # browser entrypoint: class dashboard(MainWindow)
├── widget.py           # literal __widgetset__/__version__ metadata
├── dashboard_data.py   # decorated BFF class; replaced by a browser stub
└── helpers.py          # statically imported browser code
```

`GET /{application}` serves the loader page, where `{application}` is the
**module filename** — `/dashboard` runs `dashboard.py`. It is not the class
name; those merely coincide when the class is named after its module.

Pytincture finds the browser entrypoint statically, without importing the module.
Supported forms: a top-level class or callable named the same as the application;
a top-level class directly inheriting `dhxpyt.layout.MainWindow`; or literal
metadata such as `APP_ENTRYPOINT = "Dashboard"`.

## widget.py is required

The backend resolves which widgetset wheel to install by walking the
entrypoint's **imports** looking for literal metadata, so the entrypoint must
import it:

```python
# widget.py
__widgetset__ = "dhxpyt"
__version__ = "0.9.18"
```

```python
# dashboard.py
import widget
from dhxpyt.layout import MainWindow
```

Both values must be literals; the backend parses them with `ast` and never
imports the module.

## ASGI factory (recommended)

```python
from pathlib import Path
from pytincture import PytinctureConfig, create_app

HERE = Path(__file__).resolve().parent
app = create_app(
    PytinctureConfig(
        modules_path=str(HERE),
        default_application="dashboard",
        cors_allowed_origins=("https://dashboard.example.com",),
    )
)
```

Run `python -m uvicorn service:app --host 127.0.0.1 --port 8070`. `create_app()`
owns its own configuration, BFF registry and state, so tests and multi-app
processes need not mutate global environment settings.

## Compatibility launcher

`launch_service()` remains supported. Put it in its **own module**, not
in the browser entrypoint: the entrypoint imports `js` and the widgetset at the
top, so `python dashboard.py` fails on the server before reaching any
`__main__` guard, and pytincture packages every import in it — guarded or not —
for the browser.

```python
# launch.py
import sys
from pathlib import Path

if __name__ == "__main__" and sys.platform != "emscripten":
    from pytincture import launch_service
    launch_service(
        modules_folder=str(Path(__file__).resolve().parent),
        default_application="dashboard",
        env_vars={"BFF_POLICY_HOOK_PATH": "launch.policy_hook"},  # if any @bff_policy
    )
```

`launch_service()` builds the app in a child process, so register hooks by
dotted path here too.

For local login, `ENABLE_USER_LOGIN` + `ENABLE_DEV_EMAIL_LOGIN` +
`ALLOWED_EMAILS` signs in by email with any password, from a literal loopback
address only. It still needs `pytincture[password]` installed (every email
login runs an argon2 check), and with any other login mode a
`SECRET_KEY` of 32+ characters plus `PYTINCTURE_ALLOWED_HOSTS`.

## Backend-for-frontend classes

```python
from pytincture.dataclass import (
    backend_for_frontend, bff_http_methods, bff_policy, bff_stream,
)

@backend_for_frontend
class Reports:
    def __init__(self, _user):
        self._user = _user

    @bff_http_methods("GET")
    @bff_policy(roles={"reader"})  # needs an identity source; see Declared policy
    def status(self):
        return {"ready": True, "email": self._user["email"]}

    @bff_stream()
    async def rows(self):
        yield {"id": 1}
```

Import the class normally from browser code; packaging strips the implementation
and emits a proxy with matching public methods. Private names and undecorated
classes are never registered.

- The proxy exposes each synchronous export twice: `name()`, a blocking XHR
  that emits a `DeprecationWarning` and is kept only for compatibility through
  1.x, and an awaitable `name_async()`. **New browser code calls the async
  companion.** The backend class does not change. `load_ui()` is synchronous,
  so schedule the call rather than blocking on it:

  ```python
  asyncio.ensure_future(self._load_dataset())   # in load_ui()

  async def _load_dataset(self):
      # ensure_future() swallows exceptions; report them explicitly.
      try:
          raw = await Reports().status_async()
      except Exception:
          import traceback
          js.console.error(traceback.format_exc())
  ```

  Async fetches, response reads and stream reads have a bounded 35-second
  browser wait on top of the server-side limits.
- Methods default to **POST**. Declaring GET asserts the method is parameterless,
  read-only, repeatable and bodyless.
- CSRF tokens are attached automatically on cookie-authenticated state changes.
- Keep secrets, database clients and file access in BFF/server modules only.
- **Never keep state in BFF module globals.** Pytincture executes the BFF
  module's source afresh for every call, so a module-level list, cache or lock
  is recreated on each request. Put state in storage, or in an ordinary module
  the BFF imports by name (that one is cached in `sys.modules` as usual).

## Declared policy

Pytincture enforces the claims it recognises **before** the hook runs, so these
keys need no hook code:

| Key | Compared against |
|---|---|
| `issuer` | `iss`/`issuer` claim |
| `tenant` | `tenant`/`tenant_id`/`tid` claim |
| `provider`, `auth_provider` | `auth_provider` claim |
| `application` | the application serving the call |
| `operation` | the exported function name |
| `role`, `roles` | caller roles — **all** declared roles are required |

A class-level `@bff_policy` merges with a method-level one key by key: the
method replaces the keys it names and inherits the rest.

Role claims exist only once an identity source supplies them — Google/Microsoft
/SAML, a `set_user_authenticator()` callable, or `AUTH_USER_CLAIMS` with
`ENABLE_USER_LOGIN`. A caller on a service with no login configured has no
roles, so **any export declaring `roles` answers 403 there**. Use
`application=` for a claim that holds under every auth mode.

Any key Pytincture does not recognise is passed to the hook untouched.

## Policy hooks

The hook is for what a declaration cannot express — request context, tenancy,
custom keys. Do not re-implement role checks in it; they have already run.

The hook contract is a **return value**, not an exception:

| Returned | Effect |
|---|---|
| `True` or `None` | allow |
| `False` | deny — Pytincture raises 403 |
| anything else | `RuntimeError` (fails closed) |

```python
# service.py
TRUSTED_INTERNAL_HOSTS = {"127.0.0.1", "::1"}

def policy_hook(user, policy, class_name, function_name, **kwargs):
    # `internal` is a custom key, so it arrives here as written.
    if policy.get("internal"):
        request = kwargs.get("request")
        client_host = request.client.host if request is not None and request.client else ""
        return client_host in TRUSTED_INTERNAL_HOSTS
    return True

app = create_app(PytinctureConfig(
    modules_path=str(HERE),
    environment={"BFF_POLICY_HOOK_PATH": "service.policy_hook"},
))
```

**Register the hook by dotted path (`BFF_POLICY_HOOK_PATH`)**, in
`PytinctureConfig(environment=...)` or the process environment. Each
`create_app()` loads its own copy of the backend module, so the module-global
`set_bff_policy_hook()` from `pytincture.backend.app` never reaches the app it
returns, and the service still refuses to start. The path must be importable
from the process: `service.policy_hook` resolves when uvicorn runs
`service:app` from that directory.

The hook is called with keyword arguments `user`, `policy`, `application`,
`class_name`, `function_name`, `module_path` and `request`.

**Registration is mandatory.** Any export carrying `@bff_policy` with no hook
registered through `BFF_POLICY_HOOK_PATH` makes the service fail closed at
startup. Async hooks are supported and are subject to the
remaining BFF call deadline.

Related hooks: `set_user_authenticator`, `revoke_session`,
`set_bff_replay_token_store`.

## Health checks

```bash
curl --fail http://127.0.0.1:8070/healthz
curl --fail http://127.0.0.1:8070/readyz
```

## Environment variables

Commonly used: `ALLOWED_EMAILS`, `ENABLE_USER_LOGIN`, `ENABLE_GOOGLE_AUTH`,
`ENABLE_SAML_AUTH`, `SECRET_KEY` (required for session signing), `DATABASE_URL`,
`BFF_POLICY_HOOK_PATH`, and the `BFF_*` limit settings. Every field of
`PytinctureConfig` has a matching variable.
