def solution(myStr):
    answer = []
    my_part=''
    for i in myStr:
        if i in 'abc':
            if my_part:
                answer.append(my_part)
                my_part =''
        else:
            my_part += i
    if my_part:
        answer.append(my_part)
    if not answer:
        return ['EMPTY']
    return answer