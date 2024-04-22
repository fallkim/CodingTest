def solution(rank, attendance):
    answer = [(rank[i], attendance[i],i) for i in range(len(rank))]
    genius = [i for i in answer if i[1]]
    
    genius.sort()
    
    if len(genius) >= 3:
        a,b,c = genius[0][2],genius[1][2],genius[2][2]
    else:
        return -1
    
    return 10000 * a + 100 * b + c