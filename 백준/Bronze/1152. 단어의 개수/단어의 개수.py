S = input()
S = S.strip(' ')
if S == '':
  print(0)
else:
  print(S.count(' ')+1)