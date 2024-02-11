def solution(myString, pat):
    answer = myString.rfind(pat)
    if answer != -1:
        return myString[:answer + len(pat)]
    