"""
ASGI entrypoint for service mode (the recommended Pytincture 1.0 pattern).

Run with:  python -m uvicorn service:app --host 127.0.0.1 --port 8070
Then open: http://127.0.0.1:8070/py_ui

create_app() owns its own configuration, BFF registry and state, so tests and
multi-app processes do not have to mutate global environment settings.
`launch_service()` (see the bottom of py_ui.py) remains supported for existing
code.
"""
from pathlib import Path

from pytincture import PytinctureConfig, create_app

HERE = Path(__file__).resolve().parent

TRUSTED_INTERNAL_HOSTS = {"127.0.0.1", "::1"}


def policy_hook(user, policy, class_name, function_name, **kwargs):
    """Extra authorization for exports that carry @bff_policy.

    Pytincture has already enforced every claim it recognises before this
    runs: issuer, tenant, provider, auth_provider, application, operation and
    role/roles, the last requiring ALL of the declared roles. Do not
    re-implement those here -- the hook exists for the checks a declaration
    cannot express, and it receives the keys Pytincture does not know.

    The contract is a return value, not an exception:
      True or None  -> allow
      False         -> deny (Pytincture raises 403)
      anything else -> RuntimeError, so the call fails closed.

    `user` holds the caller's claims. kwargs carries `request` (the FastAPI
    Request, for IP/tenant/header checks), plus `application` and
    `module_path`.
    """
    if policy.get("internal"):
        request = kwargs.get("request")
        client_host = request.client.host if request is not None and request.client else ""
        return client_host in TRUSTED_INTERNAL_HOSTS
    return True


# Mandatory whenever any export carries @bff_policy: without a hook the service
# refuses to start. Register it by dotted path; set_bff_policy_hook() does not
# reach an app built by create_app(), which loads its own backend module copy.
app = create_app(
    PytinctureConfig(
        modules_path=str(HERE),
        default_application="py_ui",
        environment={"BFF_POLICY_HOOK_PATH": "service.policy_hook"},
    )
)
