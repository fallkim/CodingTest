def solution(myString, pat):
    a = b =0
    while True:
        b = myString.find(pat, b)
        if b == -1:
            break
        a +=1
        b+=1
    return a