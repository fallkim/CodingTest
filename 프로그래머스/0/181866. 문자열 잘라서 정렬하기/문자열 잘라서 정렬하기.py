def solution(myString):
    answer = myString.split('x')
    parts = [i for i in answer if i]
    answer1 = sorted(parts)
    return answer1