N = int(input())
total = 0
maximum = 0
i = 0
grade = []
grade = input().split()

while i != N:
  if int(grade[i]) > maximum:
    maximum = int(grade[i])
  i += 1
for j in range(N):
  total += int(grade[j])/maximum*100
print(total/N)