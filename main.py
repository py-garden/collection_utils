from typing import Dict, Optional, TypeVar, Hashable

K = TypeVar('K', bound=Hashable)
V = TypeVar('V', bound=Hashable)

def is_dict_invertible(d: Dict[K, V]) -> bool:
    values = list(d.values())
    return len(values) == len(set(values))

def invert_dict(d: Dict[K, V]) -> Optional[Dict[V, K]]:
    if not is_dict_invertible(d):
        return None
    return {v: k for k, v in d.items()}

def are_elements_unique(lst: list) -> bool:
    """
    Verify if all elements in a list are unique.

    :param lst: List of elements to check
    :return: True if all elements are unique, False otherwise
    """
    return len(lst) == len(set(lst))
