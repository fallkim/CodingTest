def solution(my_string):
    answer = 0
    n =''
    for i in my_string:
        if i.isdigit():
            n +=i
        else:
            if n:
                answer += int(n)
                n = ''
    if n :
        answer += int(n)
    return answer