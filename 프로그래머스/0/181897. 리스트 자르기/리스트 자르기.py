def solution(n, slicer, num_list):
    answer = []
    a = slicer[0]
    b = slicer[1] +1
    c = slicer[2]
        
    if n == 1:
        answer = num_list[:b]
    elif n ==2:
        answer = num_list[a:]
    elif n == 3:
        answer = num_list[a:b]
    elif n == 4:
        answer = num_list[a:b:c]
    return answer