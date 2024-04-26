def solution(score):
    answer = [sum(s) /2 for s in score]
    
    rank = [0] * len(score)
    for i in range(len(score)):
        a =1
        for j in range(len(score)):
            if i != j and answer[j] > answer[i]:
                 a +=1
        rank[i] = a
    return rank