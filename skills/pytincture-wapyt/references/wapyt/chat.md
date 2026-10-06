# wapyt.chat

Generated from wapyt 0.1.0 source by `scripts/generate_reference.py`.

## Config and data classes

### ChatAgentConfig
Describes the assistant/agent that powers the chat experience.

Args:
    name: Display name rendered in the header (defaults to ``"Assistant"``).
    subtitle: Optional subtitle shown below the name.
    avatar: URL for the avatar image; falls back to initials when missing.
    accent_color: Hex/rgb color used for accents when the theme supports it.
    tagline: Short description surfaced in layouts that show agent cards.
    extra: Free-form mapping merged into the JS payload for custom props.

```python
ChatAgentConfig(
    name: str = 'Assistant',
    subtitle: Optional[str] = None,
    avatar: Optional[str] = None,
    accent_color: Optional[str] = None,
    tagline: Optional[str] = None,
    extra: Dict[str, Any] = field(default_factory=dict),
)
```

### ChatConfig
High-level configuration object for the Chat widget.

Common fields:

* ``messages`` – initial transcript (list of :class:`ChatMessageConfig`).
* ``storage_key`` – enables persistence via localStorage when set.
* ``layout_mode`` / ``layout_density`` – tweak compact/advanced UI.
* ``extra`` – attached verbatim to the JS config for experiments.

Most fields are optional; unspecified values fall back to sensible defaults
so AI agents can produce minimal configs and rely on feature detection.

```python
ChatConfig(
    agent: ChatAgentConfig = field(default_factory=ChatAgentConfig),
    messages: List[Union[ChatMessageConfig, Dict[str, Any]]] = field(default_factory=list),
    input_placeholder: str = 'Message the assistant…',
    send_button_text: str = 'Send',
    composer_help_text: Optional[str] = 'Shift+Enter for a newline',
    composer_max_height: Optional[int] = None,
    theme: str = 'auto',
    auto_append_user_messages: bool = True,
    enable_artifacts: bool = True,
    artifact_panel_width: Optional[int] = None,
    max_messages: Optional[int] = None,
    streaming_debounce_ms: int = 32,
    id_prefix: Optional[str] = None,
    demo_response: Optional[str] = None,
    storage_key: Optional[str] = None,
    default_model: Optional[str] = None,
    voice_input: bool = False,
    voice_max_seconds: int = 120,
    voice_continuous: bool = False,
    vad_threshold: float = 0.015,
    vad_silence_ms: int = 800,
    extra: Dict[str, Any] = field(default_factory=dict),
    layout_mode: str = 'advanced',
    layout_density: str = 'comfortable',
    layout_show_sidebar: bool = True,
)
```

### ChatMessageConfig
Represents a single chat message rendered within the widget.

Args:
    role: ``"user"``, ``"assistant"``, ``"system"``, or any custom label.
    content: Markdown/HTML-safe text to render inside the transcript.
    id: Optional identifier for later updates via ``update_message``.
    name: Display name (defaults to role-specific fallback).
    timestamp: ISO timestamp string for chronological context.
    avatar: Optional avatar URL for per-message overrides.
    meta: Extra data forwarded to event handlers.
    streaming: Flag indicating the message is still streaming.
    actions: Optional list of per-message buttons (dict payloads).

```python
ChatMessageConfig(
    role: str,
    content: str,
    id: Optional[str] = None,
    name: Optional[str] = None,
    timestamp: Optional[str] = None,
    avatar: Optional[str] = None,
    meta: Dict[str, Any] = field(default_factory=dict),
    streaming: bool = False,
    actions: Optional[List[Dict[str, Any]]] = None,
)
```

## Widget classes

### Chat
Python wrapper around the custom Chat widget.

Quick start::

    layout = Layout(LayoutConfig(rows=[CellConfig(id="chat", grow=1)]))
    chat = layout.add_chat("chat", ChatConfig())
    chat.on_send(lambda payload: print("User sent:", payload["content"]))

The widget exposes helpers for streaming updates (`start_stream`,
`append_stream`, `finish_stream`) so LLM-driven agents can incrementally
render responses while work is still in progress.

```python
Chat(config: Optional[ChatConfig] = None, *, container: Any = None, root: Optional[Union[str, Any]] = None)
```

```python
on_send(handler: Callable[[Dict[str, Any]], Any]) -> None  # Fired when the user submits a prompt from the composer. Handler receives a payload with message text and identifiers.
on_voice(handler: Callable[[Dict[str, Any]], Any]) -> None  # Fired when a push-to-talk recording finishes.
on_voice_error(handler: Callable[[Dict[str, Any]], Any]) -> None  # Fired when capture could not start -- permission denied, no device, or a Permissions-Policy that blocks the microphone.
apply_transcript(text: str, *, submit: bool = False) -> None  # Write a transcript into the composer.
set_composer_text(text: str, *, append: bool = False, submit: bool = False) -> None  # Put text into the composer. Used to deliver a transcript.
on_artifact_save(handler: Callable[[Dict[str, Any]], Any]) -> None  # Fired when the user requests to save/download an artifact.
on_artifact_load(handler: Callable[[Dict[str, Any]], Any]) -> None  # Fired after a user picks a file to load into the artifact preview pane.
on_copy(handler: Callable[[Dict[str, Any]], Any]) -> None  # Fired when the user clicks the per-message copy button.
set_messages(messages: Iterable[Union[ChatMessageConfig, Dict[str, Any]]]) -> None
add_message(message: Union[ChatMessageConfig, Dict[str, Any]]) -> str
update_message(message_id: str, **updates) -> None
remove_message(message_id: str) -> None
clear_messages() -> None
start_stream(message: Union[ChatMessageConfig, Dict[str, Any]]) -> str
append_stream(message_id: str, chunk: str) -> None
finish_stream(message_id: str, final_chunk: Optional[str] = None) -> None
set_agent(agent: Union[ChatAgentConfig, Dict[str, Any]]) -> None
set_extra(extra: Dict[str, Any]) -> None  # Replace the model catalogue after construction and rebuild the selector.
set_models(models: List[str]) -> None
set_theme(theme: str) -> None
focus_composer() -> None
set_chat_badge(chat_id: str, badge: Optional[int]) -> None
get_chats() -> List[Dict[str, Any]]
get_messages(chat_id: Optional[str] = None) -> List[Dict[str, Any]]
build_history(*, chat_id: Optional[str] = None, system_prompt: Optional[str] = None, exclude_ids: Optional[Iterable[str]] = None, include_empty: bool = False) -> List[Dict[str, str]]
extract_stream_error(chunk: Any) -> Optional[str]  # Return a human-readable message when ``chunk`` is an error payload.
extract_stream_text(chunk: Any) -> str
consume_stream(response_id: str, stream: Any, *, parser: Optional[Callable[[Any], str]] = None, finish: bool = True, on_error: Optional[Callable[[Exception], None]] = None) -> None
destroy() -> None
```

### ChatStreamError
Raised when a backend stream yields an error payload instead of content.

Streaming backends report provider failures in-band (see
``tests/multiaiproxy.py``), so a failed call still looks like a normal
stream of chunks. Surfacing it as an exception routes it through the same
handling as a transport error.
