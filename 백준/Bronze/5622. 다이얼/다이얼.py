S = input()
num = 0
for i in S:
  if i == 'A' or i == 'B' or i == 'C':
    num+=3
  elif i == 'D' or i == 'E' or i == 'F':
    num+=4
  elif i == 'G' or i == 'H' or i == 'I':
    num+=5
  elif i == 'J' or i == 'K' or i == 'L':
    num+=6
  elif i == 'M' or i == 'N' or i == 'O':
    num+=7
  elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':
    num+=8
  elif i == 'T' or i == 'U' or i =='V':
    num+=9
  else:
    num+=10
print(num)