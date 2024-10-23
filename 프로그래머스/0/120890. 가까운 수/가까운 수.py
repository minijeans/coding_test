def solution(array, n):
    array_minus = []
    temp = array[0]
    min_num = abs(array[0] - n)
    answer = array[0]
    for i in range(len(array)):
        if abs(array[i] - n) < min_num:
            min_num = abs(array[i] - n)
            answer = array[i]
            temp = array[i]
        elif abs(array[i] - n) == min_num and temp > array[i]:
            answer = array[i]
    return answer