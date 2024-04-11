def solution(spell, dic):
    answer = sorted(spell)
    for i in dic:
        if sorted(i) == answer:
            return 1
    return 2