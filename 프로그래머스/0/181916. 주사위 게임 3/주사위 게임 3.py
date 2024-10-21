def solution(a, b, c, d):
    n_list = [a, b, c, d]
    if len(set(n_list)) == 1:
        return 1111*a
    elif len(set(n_list)) == 2:
        for i in range(1, 7):
            if n_list.count(i) == 3:
                j = list(set(n_list) - set([i]))[0]
                return (10*i+j)**2
            elif n_list.count(i) == 2:
                j = list(set(n_list) - set([i]))[0]
                if i > j:
                    return (i+j)*(i-j)
                else:
                    return(i+j)*(j-i)
    elif len(set(n_list)) == 3:
        for i in range(1, 7):
            if n_list.count(i) == 2:
                return list(set(n_list) - set([i]))[0]*list(set(n_list) - set([i]))[1]
    else:
        return min(n_list)