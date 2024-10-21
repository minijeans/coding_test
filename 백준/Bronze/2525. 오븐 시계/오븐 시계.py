A, B = map(int, input().split())
C = int(input())
answer = A*60 + B + C
A = answer // 60
B = answer % 60
if A >= 24:
  A = A-24
print(A, B)