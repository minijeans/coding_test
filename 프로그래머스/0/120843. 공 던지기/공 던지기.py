def solution(numbers, k):
    if len(numbers)%2 == 0:
        n_list = numbers[::2]
        return n_list[k%len(n_list)-1]
    else:
        n_list = numbers[::2] + numbers[1::2]
        return n_list[k%len(n_list)-1]