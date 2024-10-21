def solution(arr):
    i = 0 
    stk = []
    while i != len(arr):
        if stk == []:
            stk.append(arr[i])
            i += 1
        elif len(stk) == 1 and stk[0] < arr[i]:
            stk.append(arr[i])
            i += 1
        elif stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        else:
            stk.remove(stk[-1])
    return stk