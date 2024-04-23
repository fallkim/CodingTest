def solution(emergency):
    answer = []
    answer1 = []
    
    answer1 = sorted(emergency)
    answer1.reverse()
    
    for i in emergency:
        answer.append(answer1.index(i)+1)
    return answer