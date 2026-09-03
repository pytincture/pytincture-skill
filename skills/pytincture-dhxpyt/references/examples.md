# Bundled examples

## Full app (service mode)

`assets/examples/pytincture_app/`

| File | Role |
|---|---|
| `service.py` | ASGI entrypoint using `create_app` + `PytinctureConfig` |
| `py_ui.py` | browser entrypoint: layout, sidebar, toolbar, tabbar, grid, chart, calendar, form |
| `py_ui_data.py` | `@backend_for_frontend` class supplying data |
| `widget.py` | literal `__widgetset__`/`__version__` for the backend |
| `dataset.json`, `reconciliation.json` | sample data |

Run it:

```bash
cd assets/examples/pytincture_app
python -m uvicorn service:app --port 8070   # then open http://127.0.0.1:8070/py_ui
```

`py_ui.py` also carries a guarded `launch_service()` block showing the
compatibility launcher.

`load_ui()` builds the widgets and returns; `_load_dataset()` then awaits
`py_ui_data().dataset_async()` and fills the grid and the ratings chart. That
is the pattern to copy — the plain `dataset()` proxy is a blocking XHR and is
deprecated through 1.x.

### What the BFF policy in this example demonstrates

Pytincture enforces the claims it recognises -- `issuer`, `tenant`,
`provider`, `auth_provider`, `application`, `operation`, `role`/`roles` --
itself, before the registered policy hook runs. `roles` requires **all** of
the declared roles, and role claims exist only once an identity source
supplies them. A `roles` requirement on an export that a no-login service has
to serve is therefore an unconditional 403; that is the usual cause of an
example that renders its shell but never fills its grid.

So the example splits the two cases:

- `dataset()`, which `py_ui` loads at startup, inherits only
  `@bff_policy(application="py_ui")`. That claim is compared against the
  running application, so it is enforced under every auth mode -- including
  the no-login service above -- and still stops another application from
  reusing the export.
- `reconciliation_dataset()` adds `roles={"manager"}` and `internal=True`. It
  is reachable once an identity source supplies the role: Google/Microsoft/
  SAML, a `set_user_authenticator()` callable, or `AUTH_USER_CLAIMS` with
  `ENABLE_USER_LOGIN`, as the `launch_service()` block at the bottom of
  `py_ui.py` shows.

`internal` is not a claim Pytincture knows, so it passes through to the hook
untouched -- which is what a policy hook is for. Do not re-implement role
checks there; the framework has already run them, and a hook that intersects
roles instead of requiring all of them only documents a rule the service does
not follow.

## Minimal UI (dhxpyt)

`assets/examples/dhxpyt_ui/testui.py` — layout + toolbar + grid.

Both examples implement `load_ui()` only and never override `__init__` to call
it; see [`dhxpyt.md`](dhxpyt.md) for why that matters.

## Standalone template

`assets/standalone/index.html` — static, browser-only page with inline Python,
a pinned `micropip-libs` block, and self-hosted runtime instructions.
