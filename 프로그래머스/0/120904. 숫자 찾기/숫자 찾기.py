def solution(num, k):
    
    num_list = list(map(int, str(num)))
    
    for i, digit in enumerate(num_list):
        if digit == k:
            return i+1            
    return -1