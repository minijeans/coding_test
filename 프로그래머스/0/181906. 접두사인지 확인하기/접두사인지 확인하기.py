def solution(my_string, is_prefix):
    my_list = [my_string[:i+1] for i in range(len(my_string))]
    return int(is_prefix in my_list)