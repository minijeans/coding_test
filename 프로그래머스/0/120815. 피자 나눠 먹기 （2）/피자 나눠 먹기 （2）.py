def solution(n):
    result = 1
    while (6 * result) % n != 0:
        result += 1
    return result