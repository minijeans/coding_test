def solution(numLog):
    answer = ''
    i = 0
    while len(numLog) != i+1:
        if numLog[i+1] - numLog[i] == 1:
            answer += "w"
        elif numLog[i+1] - numLog[i] == -1:
            answer += "s"
        elif numLog[i+1] - numLog[i] == 10:
            answer += "d"
        else:
            answer += "a"
        i += 1
    return answer