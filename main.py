def are_elements_unique(lst: list) -> bool:
    """
    Verify if all elements in a list are unique.

    :param lst: List of elements to check
    :return: True if all elements are unique, False otherwise
    """
    return len(lst) == len(set(lst))
