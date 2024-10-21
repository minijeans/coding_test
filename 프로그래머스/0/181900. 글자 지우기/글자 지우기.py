def solution(my_string, indices):
    list_my_string = list(my_string)
    for i in sorted(indices, reverse=True):
        del list_my_string[int(i)]
    return ''.join(list_my_string)