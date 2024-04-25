def solution(s):
    answer = s.split()
    result = []
    
    for i in answer:
        if i == 'Z':
            if result:
                result.pop()
        else:
            result.append(int(i))
                
    return sum(result)