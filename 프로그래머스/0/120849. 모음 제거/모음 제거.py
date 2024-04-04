def solution(my_string):
    ahdma = 'a.e.i.o.u'
    answer =''
    for char in my_string:
        if char not in ahdma:
            answer += char
    return answer