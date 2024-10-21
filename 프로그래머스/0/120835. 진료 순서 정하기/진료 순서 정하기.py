def solution(emergency):
    result = [0 for i in range(len(emergency))]
    for i in range(len(emergency)):
        result[emergency.index(max(emergency))] = i+1
        emergency[emergency.index(max(emergency))] = 0
    return result