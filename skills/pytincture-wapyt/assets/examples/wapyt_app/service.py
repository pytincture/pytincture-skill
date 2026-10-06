"""
ASGI entrypoint for a wapyt service-mode app.

Build the browser wheel into this folder first (wapyt is not on PyPI and not
in pytincture's built-in wheel locks):

    /path/to/wa_pytincture_widgetset/scripts/dev_wheel.sh .

Run with:  python -m uvicorn service:app --host 127.0.0.1 --port 8070
Then open: http://127.0.0.1:8070/inventory
"""
from pathlib import Path

from pytincture import PytinctureConfig, create_app

HERE = Path(__file__).resolve().parent


def policy_hook(user, policy, class_name, function_name, **kwargs):
    """Extra authorization for exports that carry @bff_policy.

    Pytincture has already enforced the claims it recognises (application,
    roles, tenant, ...) before this runs. The contract is a return value:
    True/None allow, False denies with 403, anything else fails closed.
    """
    return True


# Mandatory whenever any export carries @bff_policy: without a hook the
# service refuses to start. Register it by dotted path in the config.
# set_bff_policy_hook() does NOT work with create_app(): each app loads its own
# copy of the backend module, so the module-global setter never reaches it.
app = create_app(
    PytinctureConfig(
        modules_path=str(HERE),
        default_application="inventory",
        environment={"BFF_POLICY_HOOK_PATH": "service.policy_hook"},
    )
)
