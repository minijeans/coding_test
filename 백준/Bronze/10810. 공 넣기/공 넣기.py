N, M = map(int, input().split())
n_list = [0 for i in range(N)]
for z in range(M):
  i, j, k = map(int, input().split())
  for c in range(j-i+1):
    n_list[i-1] = k
    i += 1
for i in range(N):
  print(n_list[i], end = ' ')