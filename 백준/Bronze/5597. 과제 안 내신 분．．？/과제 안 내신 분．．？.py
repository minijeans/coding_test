students = [i for i in range(1, 31)]
submit = [int(input()) for i in range(28)]

print(min(set(students) - set(submit)), max(set(students) - set(submit)), sep ='\n')