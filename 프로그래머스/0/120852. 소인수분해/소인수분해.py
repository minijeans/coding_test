def solution(n):
    result = []
    for i in range(n+1):
        if n % (i+2) == 0:
            result.append(i+2)
            while n % (i+2) == 0:
                n = n // (i+2)
    return result