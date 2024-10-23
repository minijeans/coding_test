def solution(order):
    result = 0
    num = 0
    while order != 0:
        num = order % 10 
        if num == 3 or num == 6 or num == 9:
            result += 1
        order //= 10
    return result