def solution(my_string, s, e):
    a = my_string[s:e+1]
    return my_string[:s]+a[::-1]+my_string[e+1:]