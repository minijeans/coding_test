num_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N, B = map(int, input().split())
num = 0
result = ''
while N >= B:
  num = N % B
  result += num_list[int(num)]
  N //= B
result += num_list[N]
print(result[::-1])