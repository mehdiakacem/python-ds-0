def count_in_list(items, value):
    """Count occurrences of a value in a list."""
    count = 0
    for item in items:
        if item == value:
            count += 1
    return count
