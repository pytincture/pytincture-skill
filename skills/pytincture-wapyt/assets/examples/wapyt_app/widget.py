"""
Browser widget metadata, read by the Pytincture backend without importing it.

Service mode walks the entrypoint's imports for literal `__widgetset__` /
`__version__` and pins the browser install to `wapyt==0.1.0`. wapyt is not in
pytincture's built-in wheel locks and is not on PyPI, so the wheel itself must
sit in this folder: build it with wapyt's `scripts/dev_wheel.sh <this folder>`.
"""

__widgetset__ = "wapyt"
__version__ = "0.1.0"
