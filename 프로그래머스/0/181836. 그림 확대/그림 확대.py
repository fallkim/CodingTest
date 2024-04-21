def solution(picture, k):
    answer = []
    for i in picture:
        row = ''.join(char*k for char in i)
        for _ in range(k):
            answer.append(row)
    return answer