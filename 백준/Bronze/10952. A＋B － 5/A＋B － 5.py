A, B = map(int, input().split())
print(A+B)

while A != 0 and B != 0:
  A, B = map(int, input().split())
  if A == 0 and B == 0:
    break
  print(A+B)
