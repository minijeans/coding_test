def solution(num_list):
    a = 1
    for i in num_list:
        a *= i 
    return 1 if a < sum(num_list)**2 else 0