from typing import (
    Collection,
    Iterable,
)

from pandas._typing import T

def flatten(line) -> None: ...
def consensus_name_attr(objs): ...
def is_bool_indexer(key) -> bool: ...
def cast_scalar_indexer(val): ...
def not_none(*args): ...
def any_none(*args): ...
def all_none(*args): ...
def any_not_none(*args): ...
def all_not_none(*args): ...
def count_not_none(*args): ...
def asarray_tuplesafe(values, dtype=...): ...
def index_labels_to_array(labels, dtype=...): ...
def maybe_make_list(obj): ...
def maybe_iterable_to_list(obj: Iterable[T] | T) -> Collection[T] | T: ...
def is_null_slice(obj): ...
def is_true_slices(line): ...
def is_full_slice(obj, line): ...
def get_callable_name(obj): ...
def apply_if_callable(maybe_callable, obj, **kwargs): ...
def standardize_mapping(into): ...
def random_state(state=...): ...
def pipe(obj, func, *args, **kwargs): ...
def get_rename_function(mapper): ...
