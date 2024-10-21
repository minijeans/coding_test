N, M = map(int, input().split())
n_list = [i+1 for i in range(N)]
for k in range(M):
  i, j = map(int, input().split())
  n_list[i-1], n_list[j-1] = n_list[j-1], n_list[i-1]
for i in range(N):
  print(n_list[i], end = ' ')