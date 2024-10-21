S = input()
n_list = [-1 for i in range(26)]

for i in range(97, 123):
  n_list[i-97] = S.find(chr(i))

for i in n_list:
  print(i, end = ' ')