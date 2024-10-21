def solution(num_list, n):
    answer = []
    answer.append([num_list[i*n:(i+1)*n] for i in range(len(num_list)//n)])
    return answer[0]