N = int(input())
num = []
num.append(input().split())
v = input()
k = 0
for i in range(int(N)):
  if num[0][i] == v:
    k = k+1
print(k)