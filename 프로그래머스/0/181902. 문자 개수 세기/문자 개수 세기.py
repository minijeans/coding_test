def solution(my_string):
    answer=[]
    for i in range(52):
        if i < 26:
            answer.append(my_string.count(chr(65+i)))
        else:
            answer.append(my_string.count(chr(71+i)))
    return answer