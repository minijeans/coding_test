def solution(numer1, denom1, numer2, denom2):
        denom = denom1 * denom2
        numer = numer1 * denom2 + numer2 * denom1
        if denom > numer:
            for i in range (denom):
                if denom % (denom-i) == 0 and numer % (denom-i) == 0:
                    denom_answer = denom // (denom-i)
                    numer_answer = numer // (denom-i)
                    return [numer_answer, denom_answer]
        else:
            for i in range (numer):
                if denom % (numer-i) == 0 and numer % (numer-i) == 0:
                    denom_answer = denom // (numer-i)
                    numer_answer = numer // (numer-i)
                    return [numer_answer, denom_answer]