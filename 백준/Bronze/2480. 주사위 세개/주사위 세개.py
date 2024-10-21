A, B, C = map(int, input().split())
if A == B == C:
  answer = 10000 + A * 1000
elif A == B or B == C or C == A:
  if A == B:
    answer = 1000 + A * 100
  elif B == C:
    answer = 1000 + B * 100
  else:
    answer = 1000 + C * 100
else:
  answer = max(A,B,C) * 100
print(answer)