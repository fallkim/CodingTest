def solution(polynomial):
    x=0
    y=0
    t=polynomial.split(' + ')
    
    for i in t:
        if 'x' in i:
            if i =='x':
                x +=1
            else:
                x += int(i[:-1])
        else:
            y += int(i)
    
    answer =[]
    if x != 0:
        if x ==1:
            answer.append('x')
        else:
            answer.append(f"{x}x")
    if y != 0:
        answer.append(str(y))
    
    return ' + '.join(answer) if answer else '0'