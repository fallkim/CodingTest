def solution(my_string, indices):
    a_list = list(my_string)
    for i in sorted(indices, reverse=True):
        if i < len(a_list):
            del a_list[i]
        
    return ''.join(a_list)