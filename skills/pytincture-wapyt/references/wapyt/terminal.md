# wapyt.terminal

Generated from wapyt 0.1.0 source by `scripts/generate_reference.py`.

## Config and data classes

### TerminalConfig
Controls :class:`Terminal` rendering and its WebSocket transport.

Args:
    ws_url: WebSocket endpoint for the shell relay. A path such as
        ``"/ws/terminal/7"`` is resolved against the current origin, so it
        follows http/https to ws/wss automatically. When omitted the
        terminal renders but does not connect; call ``connect()`` later.
    asset_base: Origin-relative directory serving ``xterm.js``,
        ``xterm.css``, ``addon-fit.js`` and (optionally)
        ``addon-search.js``. xterm is deliberately *not* bundled into the
        widgetset — see the note in ``assets/terminal.js``.
    font_family: CSS font stack for the terminal grid.
    font_size: Font size in pixels.
    scrollback: Lines of scrollback retained.
    theme: Optional :class:`TerminalTheme`.
    search: Load the search addon and bind Ctrl+F to the search bar.
    clipboard: Copy and paste the way Windows Terminal does: Ctrl+C copies
        a selection (and interrupts without one), Ctrl+Shift+C always
        copies, Ctrl+V and Ctrl+Shift+V paste, Cmd on a Mac; plus a
        right-click menu. Costs the ability to send a literal Ctrl+V.
    reconnect: Reconnect automatically when the socket drops.
    reconnect_max_attempts: Give up after this many consecutive failures.
    reconnect_base_ms: First backoff delay; doubles per attempt.
    fit_debounce_ms: Wait this long after the container stops changing size
        before re-fitting. 0 (the default) fits on every ResizeObserver
        callback, which is right for a container that only changes size
        occasionally. Set it (~120) when the container can be dragged: a
        resize drag otherwise sends a PTY resize per frame, and the remote
        redraws for every one of them. An explicit ``fit()`` is never
        debounced.
    cursor_blink: Whether the cursor blinks.
    extra: Additional properties forwarded to JS verbatim.

```python
TerminalConfig(
    ws_url: Optional[str] = None,
    asset_base: str = '/xterm',
    font_family: Optional[str] = None,
    font_size: Optional[int] = None,
    scrollback: Optional[int] = None,
    theme: Optional[TerminalTheme] = None,
    search: bool = True,
    clipboard: bool = True,
    reconnect: bool = True,
    reconnect_max_attempts: int = 5,
    reconnect_base_ms: int = 1000,
    fit_debounce_ms: int = 0,
    cursor_blink: bool = True,
    extra: Dict[str, Any] = field(default_factory=dict),
)
```

### TerminalTheme
xterm colour theme. Every field is optional; unset entries fall back to
xterm's own defaults.

```python
TerminalTheme(
    background: Optional[str] = None,
    foreground: Optional[str] = None,
    cursor: Optional[str] = None,
    cursor_accent: Optional[str] = None,
    selection_background: Optional[str] = None,
)
```

## Widget classes

### Terminal
A connected terminal pane.

Quick start::

    term = Terminal(
        TerminalConfig(ws_url=f"/ws/terminal/{session_id}"),
        container=tabs.get_cell("term_1"),
    )
    term.on_disconnect(lambda payload: print("closed", payload))

**Terminal bytes never cross into Python.** Keystrokes go from xterm
straight to the socket, and output goes straight to the screen, entirely
inside ``assets/terminal.js``. Pyodide is single-threaded on the main
thread, so an FFI hop per keypress and per output frame is exactly what
makes a browser terminal feel laggy. This wrapper drives lifecycle only:
connect, resize, search, focus, tear down.

```python
Terminal(config: Optional[TerminalConfig] = None, *, container: Any = None, root: Optional[Union[str, Any]] = None)
```

```python
on_ready(handler: Callable[[Dict[str, Any]], Any]) -> None  # Terminal constructed and xterm assets loaded.
on_connect(handler: Callable[[Dict[str, Any]], Any]) -> None  # Relay reported a live shell; payload carries ``host``.
on_disconnect(handler: Callable[[Dict[str, Any]], Any]) -> None  # Socket closed; payload carries ``code`` and ``clean``.
on_error(handler: Callable[[Dict[str, Any]], Any]) -> None
on_reconnecting(handler: Callable[[Dict[str, Any]], Any]) -> None  # Backoff started; payload carries ``attempt`` and ``delay``.
on_reconnect_failed(handler: Callable[[Dict[str, Any]], Any]) -> None
on_title(handler: Callable[[Dict[str, Any]], Any]) -> None  # Remote set the window title (OSC 0/2); payload carries ``title``.
on_copy(handler: Callable[[Dict[str, Any]], Any]) -> None  # Selection copied to the clipboard; payload carries ``chars``.
on_clipboard_error(handler: Callable[[Dict[str, Any]], Any]) -> None  # The browser refused a copy or paste; payload carries ``action`` and a human-readable ``message``.
connect() -> None
disconnect() -> None
reconnect() -> None
fit() -> None  # Re-measure and push the new size to the relay.
focus() -> None
copy_selection() -> None  # Copy the current selection (as Ctrl+Shift+C does).
paste_clipboard() -> None  # Paste from the clipboard. The browser may ask the user first.
write(text: str) -> None  # Write directly to the screen (local notices, not remote input).
clear() -> None
show_search() -> None
hide_search() -> None
toggle_search() -> None
destroy() -> None  # Close the socket, drop observers and empty the host element.
```
