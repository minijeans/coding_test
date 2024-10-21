def solution(arr, queries):
    answer = []
    result = []
    for s, e, k in queries:
        while s != e+1:
            if arr[s] > k:
                answer.append(arr[s])
            s += 1
        if answer != []:
            result.append(min(answer))
        else:
            result.append(-1)
        answer = []
    return result