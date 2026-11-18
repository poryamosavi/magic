def binary_search_and_stats_33(arr: list[int], target: int) -> dict:
    sorted_arr = sorted(arr)
    low, high, found_idx = 0, len(sorted_arr) - 1, -1
    while low <= high:
        mid = (low + high) // 2
        if sorted_arr[mid] == target:
            found_idx = mid
            break
        elif sorted_arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return {'solver_id': 33, 'sorted': sorted_arr, 'target': target, 'index': found_idx}

if __name__ == '__main__':
    print(binary_search_and_stats_33([42, 7, 19, 33, 88, 3], 33))
