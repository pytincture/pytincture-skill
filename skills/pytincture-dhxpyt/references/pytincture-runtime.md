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

## Local runtime bundle
If you want a local, non-CDN build, use the files in `assets/standalone/`.
