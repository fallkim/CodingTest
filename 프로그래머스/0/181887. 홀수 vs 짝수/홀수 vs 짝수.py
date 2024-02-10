def solution(num_list):
    a = sum(num_list[::2])
    b = sum(num_list[1::2])
    if a >b:
        return a
    elif a<b:
        return b
    else:
        return a