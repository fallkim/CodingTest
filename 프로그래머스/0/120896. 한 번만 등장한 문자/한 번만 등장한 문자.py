def solution(s):
    answer = {}
    for i in s:
        if i in answer:
            answer[i] +=1
        else:
            answer[i] =1
    char = [i for i , b in answer.items() if b ==1]
    char.sort()
    return ''.join(char)