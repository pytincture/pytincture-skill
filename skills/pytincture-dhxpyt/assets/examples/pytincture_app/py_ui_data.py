"""
Backend-for-frontend data class.

The implementation stays on the server; Pytincture packages a generated stub
with the same public methods for the browser. Keep secrets, database clients
and file access in here -- never in browser modules.
"""
from pathlib import Path

from pytincture.dataclass import backend_for_frontend, bff_policy

HERE = Path(__file__).resolve().parent


# A class-level policy applies to every export below. A method-level
# @bff_policy merges over it key by key, so a method replaces the keys it
# names and inherits the rest.
#
# Pytincture enforces the claims it recognises -- issuer, tenant, provider,
# auth_provider, application, operation, role/roles -- itself, before the
# policy hook registered in service.py runs. Any other key is passed through
# to that hook untouched.
#
# `application` is compared against the running application, so it holds under
# every auth mode, including a service with no login enabled: these exports
# answer only for /py_ui, never for a same-named class in another application.
@backend_for_frontend
@bff_policy(application="py_ui")
class py_ui_data:
    def dataset(self):
        """Loaded by py_ui at startup.

        Deliberately carries no `roles` requirement: it has to succeed under
        the no-login configuration in service.py, and an unauthenticated
        caller has no roles at all.
        """
        return (HERE / "dataset.json").read_text(encoding="utf-8")

    # `roles` requires ALL of the listed roles, and role claims exist only
    # once an identity source supplies them -- Google/Microsoft/SAML, a
    # set_user_authenticator() callable, or AUTH_USER_CLAIMS alongside
    # ENABLE_USER_LOGIN. Declaring roles on an export that a no-login service
    # must serve is the usual cause of an unexplained 403.
    #
    # `internal` is not a claim Pytincture knows, so it reaches policy_hook as
    # written and is enforced there.
    @bff_policy(roles={"manager"}, internal=True)
    def reconciliation_dataset(self):
        return (HERE / "reconciliation.json").read_text(encoding="utf-8")
