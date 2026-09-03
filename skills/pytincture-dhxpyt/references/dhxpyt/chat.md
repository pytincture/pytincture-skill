# dhxpyt.chat

Generated from dhxpyt 0.9.18 source by `scripts/generate_reference.py`.

## Config classes

### ChatAgentConfig
Describes the assistant/agent that powers the chat experience.

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

```python
ChatConfig(
    agent: ChatAgentConfig = field(default_factory=ChatAgentConfig),
    gpu: bool = False,
    gpu_widget_id: Optional[str] = None,
    messages: List[Union[ChatMessageConfig, Dict[str, Any]]] = field(default_factory=list),
    input_placeholder: str = 'Message the assistant…',
    send_button_text: str = 'Send',
    composer_help_text: Optional[str] = 'Shift+Enter for a newline',
    composer_max_height: Optional[int] = None,
    theme: str = 'auto',
    auto_append_user_messages: bool = True,
    enable_artifacts: bool = True,
    artifact_panel_open: bool = False,
    artifact_panel_width: Optional[int] = None,
    max_messages: int = 100,
    max_chats: int = 20,
    max_message_chars: int = 200000,
    max_storage_bytes: int = 2 * 1024 * 1024,
    persistence: Optional[Union[str, bool]] = None,
    include_artifact_console_in_send: bool = False,
    streaming_debounce_ms: int = 32,
    id_prefix: Optional[str] = None,
    demo_response: Optional[str] = None,
    storage_key: Optional[str] = None,
    extra: Dict[str, Any] = field(default_factory=dict),
)
```

### ChatMessageConfig
Represents a single chat message rendered within the widget.

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

```python
on_send(handler: Callable[[Dict[str, Any]], Any]) -> None
on_artifact_save(handler: Callable[[Dict[str, Any]], Any]) -> None
on_artifact_load(handler: Callable[[Dict[str, Any]], Any]) -> None
on_copy(handler: Callable[[Dict[str, Any]], Any]) -> None
on_cancel(handler: Callable[[Dict[str, Any]], Any]) -> None
set_messages(messages: Iterable[Union[ChatMessageConfig, Dict[str, Any]]]) -> None
add_message(message: Union[ChatMessageConfig, Dict[str, Any]]) -> str
update_message(message_id: str, **updates) -> None
remove_message(message_id: str) -> None
clear_messages() -> None
start_stream(message: Union[ChatMessageConfig, Dict[str, Any]]) -> str
append_stream(message_id: str, chunk: str) -> None
finish_stream(message_id: str, final_chunk: Optional[str] = None) -> None
set_agent(agent: Union[ChatAgentConfig, Dict[str, Any]]) -> None
set_theme(theme: Union[str, Dict[str, Any]], css_vars: Optional[Dict[str, Dict[str, Any]]] = None) -> None
focus_composer() -> None
set_chat_badge(chat_id: str, badge: Optional[int]) -> None
get_chats() -> List[Dict[str, Any]]
get_messages(chat_id: Optional[str] = None) -> List[Dict[str, Any]]
build_history(chat_id: Optional[str] = None, system_prompt: Optional[str] = None, exclude_ids: Optional[Iterable[str]] = None, include_empty: bool = False) -> List[Dict[str, str]]
extract_stream_text(chunk: Any) -> str
consume_stream(response_id: str, stream: Any, parser: Optional[Callable[[Any], str]] = None, finish: bool = True, on_error: Optional[Callable[[Exception], None]] = None, cancel_check: Optional[Callable[[], bool]] = None) -> None
destroy() -> None
```
