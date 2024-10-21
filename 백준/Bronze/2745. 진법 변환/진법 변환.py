N, B = map(str, input().split())
result = 0
for i in enumerate(N):
  if 64 < ord(i[1]) < 91:
    result += (ord(i[1]) - 55) * (int(B)**(len(N) - i[0] - 1))
  elif 47 < ord(i[1]) < 58:
    result += (int(i[1]) * (int(B)**(len(N) - i[0] - 1)))
  else:
    continue
print(result)