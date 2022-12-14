from collections import OrderedDict
from typing import Any, Generic, TypeVar

from humanfriendly.compat import unicode

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")

class CaseInsensitiveDict(OrderedDict[_KT, _VT], Generic[_KT, _VT]):
    def __init__(self, other: Any | None = ..., **kw) -> None: ...
    def coerce_key(self, key): ...
    @classmethod
    def fromkeys(cls, iterable, value: Any | None = ...): ...
    def get(self, key, default: Any | None = ...): ...
    def pop(self, key, default: Any | None = ...): ...
    def setdefault(self, key, default: Any | None = ...): ...
    def update(self, other: Any | None = ..., **kw) -> None: ...  # type: ignore[override]
    def __contains__(self, key): ...
    def __delitem__(self, key) -> None: ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value) -> None: ...

class CaseInsensitiveKey(unicode):
    def __new__(cls, value): ...
    def __hash__(self) -> int: ...
    def __eq__(self, other): ...
