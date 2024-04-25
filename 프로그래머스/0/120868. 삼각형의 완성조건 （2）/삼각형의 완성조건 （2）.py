def solution(sides):
    a,b = sides
    min_c = abs(a-b)+1
    max_c = a+b -1
    if min_c >max_c:
        return 0
    return max_c - min_c +1