def solution(chicken):
    answer = 0
    while chicken >= 10:
        s = chicken //10
        answer += s
        chicken = chicken % 10 + s
    return answer