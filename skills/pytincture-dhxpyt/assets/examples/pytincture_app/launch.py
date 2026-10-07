"""
Compatibility launcher: the same app through launch_service(), with user login.

Run with:  python launch.py
           (through pytincture 1.0.0rc12, first: pip install 'pytincture[password]')
Then open: http://127.0.0.1:8070/py_ui and sign in as you@example.com with any
password -- the development login skips the password check, from a literal
loopback address only (127.0.0.1, not localhost).

service.py (create_app + uvicorn) is the recommended entrypoint. This file
shows the older launch_service() path, and the login configuration that makes
py_ui_data.reconciliation_dataset() reachable.

It is its own module rather than a `__main__` block in py_ui.py: py_ui.py is
browser code that imports `js` and dhxpyt at the top, so it cannot run on the
server, and pytincture packages every import in it -- guarded or not -- for
the browser.
"""
import os
import secrets
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TRUSTED_INTERNAL_HOSTS = {"127.0.0.1", "::1"}


def policy_hook(user, policy, class_name, function_name, **kwargs):
    """
    Runs before every @backend_for_frontend call that carries @bff_policy.

    Pytincture has already enforced the claims it recognises -- issuer,
    tenant, provider, auth_provider, application, operation and role/roles,
    the last requiring ALL of the declared roles. The hook handles what a
    declaration cannot express and receives the policy keys Pytincture does
    not know.

    The contract is a return value, not an exception:
      True or None -> allow
      False        -> deny (Pytincture raises 403)
      anything else-> RuntimeError (fail closed)
    """
    if policy.get("internal"):
        request = kwargs.get("request")
        client_host = request.client.host if request is not None and request.client else ""
        return client_host in TRUSTED_INTERNAL_HOSTS
    return True


if __name__ == "__main__" and sys.platform != "emscripten":
    from pytincture import launch_service

    launch_service(
        modules_folder=str(HERE),
        default_application="py_ui",
        env_vars={
            # A @bff_policy export with no hook makes the service fail closed
            # at startup. Register it by dotted path: the app is built in a
            # child process from its own copy of the backend module, which a
            # set_bff_policy_hook() call here would never reach.
            "BFF_POLICY_HOOK_PATH": "launch.policy_hook",
            # Loopback-only development login: sign in by email, no password.
            # Production login (Google/Microsoft/SAML) additionally needs
            # PYTINCTURE_ALLOWED_HOSTS, a canonical origin and HTTPS.
            "ENABLE_USER_LOGIN": "true",
            "ENABLE_DEV_EMAIL_LOGIN": "true",
            "ALLOWED_EMAILS": "you@example.com",
            # Session signing key: at least 32 characters, 8 of them distinct,
            # or startup fails. The random fallback signs everyone out on
            # every restart; set SECRET_KEY to keep sessions.
            "SECRET_KEY": os.environ.get("SECRET_KEY") or secrets.token_urlsafe(32),
            # Login alone grants no roles. Claims configured here are what
            # make a roles-bearing export such as
            # py_ui_data.reconciliation_dataset() reachable.
            "AUTH_USER_CLAIMS": '[{"email": "you@example.com", "roles": ["manager"]}]',
        },
    )
