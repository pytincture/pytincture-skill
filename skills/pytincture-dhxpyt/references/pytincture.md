# pytincture quick reference

## What it is
- Python framework that uses Pyodide to run Python-driven UIs in the browser.
- Provides backend-for-frontend (BFF) calls and can serve full apps.
- Ships a standalone JS runtime (pytincture.js) to run embedded Python directly in HTML.

## Launch a service (backend + app delivery)
Guard the launcher so it only runs on the backend. The same module can be shipped to the frontend, so avoid running `launch_service()` under Pyodide/emscripten:

```python
import sys

if __name__ == "__main__" and sys.platform != "emscripten":
    from pytincture import launch_service
    launch_service(modules_folder=".")
```

## Backend-for-frontend (BFF) classes
Typical pattern:

```python
from pytincture.dataclass import backend_for_frontend, bff_policy

@backend_for_frontend
@bff_policy(roles={"analyst"})
class Reports:
    @bff_policy(roles={"manager"})
    def export(self):
        return {"ok": True}
```

If you want to enforce BFF policies, register a hook on the backend:

```python
from fastapi import HTTPException
from pytincture.backend.app import set_bff_policy_hook

def policy_hook(user, policy, **kwargs):
    roles = set(user.get("roles", []))
    required = policy.get("roles") or set()
    if required and not (roles & set(required)):
        raise HTTPException(status_code=403, detail="Forbidden")

set_bff_policy_hook(policy_hook)
```

## Standalone runtime (browser-only)
The runtime auto-detects `<script type="text/python">` blocks and runs them once Pyodide loads.
You can disable auto-start and call `runTinctureApp(...)` manually.

See `references/pytincture-runtime.md` for the HTML usage template.

## Environment variables
Common settings include: `ALLOWED_EMAILS`, `ENABLE_GOOGLE_AUTH`, `ENABLE_SAML_AUTH`, `DATABASE_URL`, and Redis-related vars.

## Local source locations
- `assets/standalone/index.html` and `assets/standalone/pytincture.js` are copied from the pytincture repo.
- `assets/examples/pytincture_app/` contains an end-to-end example based on pytincture_example.
