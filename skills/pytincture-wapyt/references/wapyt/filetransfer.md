# wapyt.filetransfer

Generated from wapyt 0.1.0 source by `scripts/generate_reference.py`.

## Config and data classes

### Capabilities
What the current browser will allow.

```python
Capabilities(
    save_file: bool = False,
    directory: bool = False,
    open_file: bool = False,
    secure_context: bool = False,
)
```

### PickedFile
One file chosen for upload.

```python
PickedFile(
    id: str,
    name: str,
    size: int,
    path: str,
)
```

### TransferResult
Outcome of a pick or a transfer.

```python
TransferResult(
    ok: bool,
    cancelled: bool = False,
    error: str = '',
    id: str = '',
    name: str = '',
    bytes: int = 0,
    via_anchor: bool = False,
    files: List[PickedFile] = field(default_factory=list),
    resumable: bool = False,
    retries: int = 0,
    restarted: bool = False,
)
```

## Functions

```python
capabilities() -> Capabilities
    # What this browser supports.
async pick_save_file(suggested_name: str = '') -> TransferResult
    # Native Save dialog: folder navigation and a pre-filled filename field.
async pick_folder() -> TransferResult
    # Native folder picker, for writing several files into one destination.
async pick_files(multiple: bool = True, directory: bool = False) -> TransferResult
    # Native file picker for upload.
adopt(file_object: Any) -> str
    # Register a ``File`` the page already holds — a drop, typically — so it can be uploaded through the same path as a picked one. Returns its handle id.
async save_file(handle_id: str, url: str, transfer_id: str = '', on_progress: Optional[Callable[[int, int], Any]] = None) -> TransferResult
    # Stream ``url`` into a file chosen by :func:`pick_save_file`.
async save_into(folder_id: str, relative_path: str, url: str, transfer_id: str = '', on_progress: Optional[Callable[[int, int], Any]] = None) -> TransferResult
    # Stream ``url`` into a folder chosen by :func:`pick_folder`.
download_via_anchor(url: str, suggested_name: str = '') -> TransferResult
    # Fallback download straight to the browser's download directory.
async upload(url: str, file_id: str, fields: Optional[Dict[str, Any]] = None, transfer_id: str = '', on_progress: Optional[Callable[[int, int], Any]] = None) -> TransferResult
    # POST a picked file as multipart form data, with progress.
async exists(folder_id: str, name: str) -> bool
    # Whether ``name`` is already taken, by a file or a folder, directly inside a folder chosen with :func:`pick_folder`.
async resume(transfer_id: str, on_progress: Optional[Callable[[int, int], Any]] = None) -> TransferResult
    # Carry on a download that paused after losing its connection.
cancel(transfer_id: str) -> bool
    # Abort an in-flight transfer by the id it was started with.
release(handle_id: str) -> bool
    # Drop a handle once its transfer is done.
release_all() -> None
    # Drop every retained handle — on tab close, say.
```
