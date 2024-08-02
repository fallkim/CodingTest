def solution(phone_number):
    a = len(phone_number)
    answer = (a-4)*("*") + phone_number[-4:]
    return answer