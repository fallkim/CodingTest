def solution(ineq, eq, n, m):
    answer = 0
    if (ineq =='<') and (eq =='=') and (n<=m) :
        return 1
    elif (ineq =='>') and (eq =='=') and (n>=m) :
        return 1
    elif (ineq =='>') and (eq =='!') and (n>m) :
        return 1
    elif (ineq =='<') and (eq =='!') and (n<m) :
        return 1
    else:
        return 0
        
    