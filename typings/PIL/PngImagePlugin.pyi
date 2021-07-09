from typing import Any

from ._binary import o8 as o8
from .ImageFile import ImageFile

logger: Any
is_cid: Any
MAX_TEXT_CHUNK: Any
MAX_TEXT_MEMORY: Any
APNG_DISPOSE_OP_NONE: int
APNG_DISPOSE_OP_BACKGROUND: int
APNG_DISPOSE_OP_PREVIOUS: int
APNG_BLEND_OP_SOURCE: int
APNG_BLEND_OP_OVER: int

class ChunkStream:
    fp: Any
    queue: Any
    def __init__(self, fp) -> None: ...
    def read(self): ...
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...
    def close(self) -> None: ...
    def push(self, cid, pos, length) -> None: ...
    def call(self, cid, pos, length): ...
    def crc(self, cid, data) -> None: ...
    def crc_skip(self, cid, data) -> None: ...
    def verify(self, endchunk: bytes = ...): ...

class iTXt(str):
    lang: Any
    tkey: Any
    @staticmethod
    def __new__(cls, text, lang: Any | None = ..., tkey: Any | None = ...): ...

class PngInfo:
    chunks: Any
    def __init__(self) -> None: ...
    def add(self, cid, data, after_idat: bool = ...) -> None: ...
    def add_itxt(
        self, key, value, lang: str = ..., tkey: str = ..., zip: bool = ...
    ) -> None: ...
    def add_text(self, key, value, zip: bool = ...): ...

class PngStream(ChunkStream):
    im_info: Any
    im_text: Any
    im_size: Any
    im_mode: Any
    im_tile: Any
    im_palette: Any
    im_custom_mimetype: Any
    im_n_frames: Any
    rewind_state: Any
    text_memory: int
    def __init__(self, fp) -> None: ...
    def check_text_memory(self, chunklen) -> None: ...
    def save_rewind(self) -> None: ...
    def rewind(self) -> None: ...
    def chunk_iCCP(self, pos, length): ...
    def chunk_IHDR(self, pos, length): ...
    im_idat: Any
    def chunk_IDAT(self, pos, length) -> None: ...
    def chunk_IEND(self, pos, length) -> None: ...
    def chunk_PLTE(self, pos, length): ...
    def chunk_tRNS(self, pos, length): ...
    def chunk_gAMA(self, pos, length): ...
    def chunk_cHRM(self, pos, length): ...
    def chunk_sRGB(self, pos, length): ...
    def chunk_pHYs(self, pos, length): ...
    def chunk_tEXt(self, pos, length): ...
    def chunk_zTXt(self, pos, length): ...
    def chunk_iTXt(self, pos, length): ...
    def chunk_eXIf(self, pos, length): ...
    def chunk_acTL(self, pos, length): ...
    def chunk_fcTL(self, pos, length): ...
    def chunk_fdAT(self, pos, length): ...

class PngImageFile(ImageFile):
    format: str
    format_description: str
    @property
    def text(self): ...
    fp: Any
    def verify(self) -> None: ...
    def seek(self, frame) -> None: ...
    def tell(self): ...
    decoderconfig: Any
    def load_prepare(self) -> None: ...
    def load_read(self, read_bytes): ...
    png: Any
    im: Any
    pyaccess: Any
    def load_end(self) -> None: ...
    def getexif(self): ...

def putchunk(fp, cid, *data) -> None: ...

class _idat:
    fp: Any
    chunk: Any
    def __init__(self, fp, chunk) -> None: ...
    def write(self, data) -> None: ...

class _fdat:
    fp: Any
    chunk: Any
    seq_num: Any
    def __init__(self, fp, chunk, seq_num) -> None: ...
    def write(self, data) -> None: ...

def getchunks(im, **params): ...
