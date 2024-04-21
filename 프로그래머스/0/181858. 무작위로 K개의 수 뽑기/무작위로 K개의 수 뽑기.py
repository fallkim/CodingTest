def solution(arr, k):
    seen = set()
    answer = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            answer.append(num)
        if len(answer) == k:
            return answer
    answer.extend([-1] * (k -len(answer)))
    return answer