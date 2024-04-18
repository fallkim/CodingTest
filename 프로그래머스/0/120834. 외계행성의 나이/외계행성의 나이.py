def solution(age):
    a = str(age)
    answer = ''
    for i in a:
        answer += chr(ord('a') + int(i))
    return answer