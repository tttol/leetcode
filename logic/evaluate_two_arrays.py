def evaluate(base_arr, target_arr):
    """
    Find elements in target_arr that are not present in base_arr.

    Args:
        base_arr: List of elements to use as the base for comparison
        target_arr: List of elements to check against base_arr

    Returns:
        List of elements from target_arr that are not in base_arr.
        Preserves duplicates from target_arr.

    Examples:
        >>> evaluate([1, 2, 3], [2, 3, 4, 5])
        [4, 5]
        >>> evaluate([1, 2], [3, 3, 4])
        [3, 3, 4]
    """
    base_dict: dict = {}

    for ba in base_arr:
        base_dict[ba] = 1

    ret = []
    for ta in target_arr:
        if base_dict.get(ta) is None:
            ret.append(ta)

    return ret

if __name__ == "__main__":
    base_input = input()
    base_arr = list(map(int, base_input.split(',')))

    target_input = input()
    target_arr = list(map(int, target_input.split(',')))

    result = evaluate(base_arr, target_arr)
    print(result)
