def solution(my_string):
    answer = my_string.lower()
    answer_str = sorted(answer)
    return ''.join(answer_str)