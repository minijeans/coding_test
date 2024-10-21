def solution(s):
    result = 0
    for n, i in enumerate(s.split()):
        if i == 'Z':
            result -= int(s.split()[n-1])
        else:
            result += int(s.split()[n])
    return result
                
        