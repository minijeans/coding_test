def solution(cipher, code):
    result = ''
    for i, e in enumerate(cipher):
        if (i+1) % code == 0:
            result += e
    return result