def solution(arr, idx):
    if 1 in arr[idx:]:
        if arr.index(1) < idx:
            return arr[idx:].index(1)+len(arr[:idx])
        else:
            return arr.index(1)
    else:
        return -1