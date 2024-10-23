def solution(order):
    result = 0
    num = 0
    while order != 0:
        num = order % 10 
        if num in (3, 6, 9):
            result += 1
        order //= 10
    return result