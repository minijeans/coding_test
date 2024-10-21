def solution(my_string, queries):
    my_list = [k for k in my_string]
    for i, j in queries:
        if i-1 == -1:
            my_list[i:j+1] = my_list[j::-1]
        else:
            my_list[i:j+1] = my_list[j:i-1:-1]
    return ''.join(i for i in my_list)