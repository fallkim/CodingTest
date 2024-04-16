def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isdigit():
            num = int(i)
            answer += num
    return answer