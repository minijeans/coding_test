def solution(numbers, direction):
    answer = []
    if direction == "right":
        for i in range(len(numbers)):
            answer.append(numbers[i-1])
    else:
        for i in range(len(numbers)):
            if i == len(numbers)-1:
                answer.append(numbers[0])
            else:
                answer.append(numbers[i+1])
            
    return answer