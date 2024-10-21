def solution(balls, share):
    num1 = 1
    num2 = 1
    for i in range(share):
        num1 *= balls
        num2 *= (i+1)
        balls = balls-1
    return num1/num2