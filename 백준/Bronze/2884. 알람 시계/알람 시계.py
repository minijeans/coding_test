H, M = map(int, input().split())
if H == 0:
  H = 24
answer = H*60 + M
H = (answer - 45) // 60
M = (answer - 45) % 60
if H == 24:
  H = 0
print(H, M)