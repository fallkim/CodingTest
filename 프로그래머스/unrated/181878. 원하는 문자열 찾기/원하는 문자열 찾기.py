def solution(myString, pat):
    pat_l = pat.lower()
    myString_l = myString.lower()
    if pat_l in myString_l :
        return 1
    return 0