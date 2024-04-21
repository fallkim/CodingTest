def solution(my_string):
    answer = [0] *52
    for i in my_string:
        if 'A' <= i <= 'Z':
            index = ord(i) - ord('A')
        elif 'a' <= i <= 'z':
            index = ord(i) - ord('a') +26
        answer[index] +=1
    return answer