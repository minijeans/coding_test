def solution(my_string):
    num = "0123456789"
    answer = []
    for i in my_string:
        if i in num:
            answer.append(int(i))
    answer.sort()
    return answer