# pytincture standalone mode (browser-only)

Targets pytincture **1.0.0rc5**.

Standalone mode serves ordinary static HTML. The runtime loads Pyodide, installs
the widgetset and any micropip libraries, runs inline Python, and starts the
entrypoint. There is **no BFF, no server authentication and no private Python** —
everything on the page is visible to the user. Use service mode when data or
operations need trust.

## Production setup (self-hosted, the default)

Export the verified browser assets from the installed wheel on the build machine:

```bash
python -m pip install 'pytincture==1.0.0rc5'
python -m pytincture.assets ./public/frontend
```

The export verifies every runtime, Pyodide, WASM, stdlib and icon asset against
`frontend/integrity/pytincture-1.0.0rc5.json` before copying. Then:

```html
<script>
  window.pytinctureAutoStartConfig = {
    mode: "inline",
    entrypoint: "MyApp",
    widgetlib: "dhxpyt==0.9.18",
    onLifecycleEvent: event => console.debug(event.stage, event.type)
  };
</script>
<script src="./frontend/dist/pytincture.min.js"></script>
<div id="maindiv" style="width:100%;height:100vh;"></div>
<script type="text/python">
from dhxpyt.layout import MainWindow

class MyApp(MainWindow):
    def load_ui(self):          # implement load_ui only; see dhxpyt.md
        self.set_theme("dark")
</script>
```

Serve over HTTP(S). Do **not** open the page through `file://` — browsers
restrict module, worker and network behavior for local files.

## micropip libraries must be pinned

```html
<script type="text/json" id="micropip-libs">["faker==37.0.0"]</script>
```

Every entry must be an exact `name==version` pin, or a wheel URL ending in
`#sha256=<64 hex>`. **A bare name like `["faker"]` or `["dhxpyt"]` is rejected.**
Automatic dependency resolution is disabled, so list every required package
explicitly. Packages must be pure Python or ship a Pyodide-compatible wheel — a
normal CPython native wheel cannot run in WebAssembly.

## Explicit startup

Set `window.pytinctureAutoStartDisabled = true` before loading the runtime, then:

```javascript
await window.runTinctureApp({
  mode: "inline",
  entrypoint: "MyApp",
  widgetlib: "dhxpyt==0.9.18"
});
```

The promise resolves once the entrypoint starts and rejects with
`PytinctureLifecycleError`.

## CDN mode (demos and development only)

External Pyodide fails preflight unless you supply **both** the deliberately
named `allowUnverifiedExternalPyodide: true` opt-in and SRI values copied from
the release integrity manifest:

```html
<script>
  window.pytinctureAutoStartConfig = {
    mode: "inline",
    entrypoint: "MyApp",
    widgetlib: "dhxpyt==0.9.18",
    pyodideBaseUrl: "https://cdn.example/pyodide/0.29.3/full/",
    allowUnverifiedExternalPyodide: true,
    pyodideScriptIntegrity: {
      "pyodide.js": "sha384-<trusted-manifest-value>",
      "pyodide.asm.js": "sha384-<trusted-manifest-value>"
    }
  };
</script>
<script src="https://cdn.example/pytincture/1.0.0rc5/pytincture.min.js"
        integrity="sha384-<trusted-manifest-value>"
        crossorigin="anonymous"></script>
```

WASM, the stdlib and Pyodide metadata are loaded internally by Pyodide and
cannot all receive browser SRI, so production deployments must use the
self-hosted verified runtime. A manifest fetched from the same CDN is not an
independent trust root.

## Configuration keys

The stable set includes `application`, `entrypoint`, `widgetlib`, `widgetSource`,
`widgetAssetManifest`, `mode`, `pyodideBaseUrl`, `pyodideScriptIntegrity`,
`allowUnverifiedExternalPyodide`, `loadMaterialIcons`, `materialIconsUrl`,
`materialIconsIntegrity`, `inlineSelector`, `libsSelector`, `enableBackendLogging`,
`logEndpoint`, `onLifecycleEvent`, `showLoadingOverlay`, `loadingTitle`,
`loadingOverlayId`, `enableServiceWorker`, `serviceWorkerUrl`,
`serviceWorkerScope`, `warmPyodideCache`, `devWidgetHost`, `devWheelVersion`,
`requestUuid`.

## Missing-wheel errors

A 404 for `dhxpyt-99.99.99-py3-none-any.whl` means the runtime fell through to
`devWheelVersion`, the development fallback. Pin a real version in `widgetlib`
(`"dhxpyt==0.9.18"`), or host the wheel under the application's `/appcode` folder
and reference its exact filename.

## Template

`assets/standalone/index.html` is a ready-to-fill standalone page.
