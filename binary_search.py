def binary_search(lst, item):
    low = 0
    counter = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]
        if guess == item:
            return mid, counter
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
        counter += 1
    return None, counter
