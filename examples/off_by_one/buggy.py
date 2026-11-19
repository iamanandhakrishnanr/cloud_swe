def get_last_item(items):
    # Bug: Using len(items) instead of len(items) - 1 causes an IndexError
    return items[len(items)]