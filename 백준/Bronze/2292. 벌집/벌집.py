N = int(input())
result = (N-2) // 6
i = 1
if N == 1:
  print(i)
else:
  while result > 0:
    i += 1
    result -= i
  print(i+1)