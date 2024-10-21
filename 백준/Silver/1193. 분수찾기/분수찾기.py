num = int(input())
line = 0
while num > line:
  num -= line
  line += 1
if line % 2 == 0:
  n = 1
  d = line
  for i in range(num-1):
    n += 1
    d -= 1
else:
  n = line
  d = 1
  for i in range(num-1):
    n -= 1
    d += 1
print(f"{n}/{d}")