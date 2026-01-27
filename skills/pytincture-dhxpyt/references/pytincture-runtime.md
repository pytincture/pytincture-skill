# pytincture runtime (standalone JS)

## Minimal HTML example
```html
<!DOCTYPE html>
<html>
  <head>
    <script src="https://cdn.jsdelivr.net/npm/@pytincture/runtime@0.9.20/dist/pytincture.min.js"></script>
  </head>
  <body>
    <div id="maindiv" style="width:100%;height:100vh;"></div>

    <script type="text/json" id="micropip-libs">
      ["faker"]
    </script>

    <script type="text/python">
from dhxpyt.layout import MainWindow

class Demo(MainWindow):
    def load_ui(self):
        self.set_theme("dark")
        print("Demo loaded!")
    </script>
  </body>
</html>
```

## Optional configuration
Before loading the runtime, set globals to control startup:

```html
<script>
  window.pytinctureAutoStartConfig = {
    widgetlib: "dhxpyt",
    libsSelector: "#micropip-libs",
    pyodideBaseUrl: "https://cdn.jsdelivr.net/pyodide/v0.28.0/full/",
    enableBackendLogging: false
  };
  // window.pytinctureAutoStartDisabled = true; // to call runTinctureApp manually
</script>
<script src="https://cdn.jsdelivr.net/npm/@pytincture/runtime/dist/pytincture.min.js"></script>
```

Manual start (if auto-start disabled):

```js
runTinctureApp({
  mode: "inline",
  widgetlib: "dhxpyt",
  enableBackendLogging: false
});
```

## Avoid missing wheel errors
If you see a 404 for a wheel like `dhxpyt-99.99.99-py3-none-any.whl`, the runtime is trying to load a file that doesn’t exist.

- Prefer installing from PyPI by listing `"dhxpyt"` in `#micropip-libs`:
  ```html
  <script type="text/json" id="micropip-libs">
    ["dhxpyt"]
  </script>
  ```
- If you want a local wheel, place it under your app’s `/appcode` folder and reference the exact filename.

## Local runtime bundle
If you want a local, non-CDN build, use the files in `assets/standalone/`.
