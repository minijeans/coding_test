def solution(n):
    k = 0
    answer = 0
    while (n > 1):
        k = n - 1
        while (k > 1):
            if n % k == 0:
                answer += 1
                break
            k -= 1
        n -= 1
    return answer