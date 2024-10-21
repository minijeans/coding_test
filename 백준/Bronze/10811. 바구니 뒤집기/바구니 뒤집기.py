N, M = map(int, input().split())
n_list = [i+1 for i in range(N)]
for k in range(M):
  i, j = map(int, input().split())
  if i-2 < 0:
    n_list[i-1:j] = n_list[j-1::-1]
  else:
    n_list[i-1:j] = n_list[j-1:i-2:-1]
for i in range(N):
  print(n_list[i], sep=' ')