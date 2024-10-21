def solution(arr, queries):
    for i in queries:
        s = i[0]
        e = i[1]
        for j in range(e-s+1):
            arr[e-j] += 1
    return arr