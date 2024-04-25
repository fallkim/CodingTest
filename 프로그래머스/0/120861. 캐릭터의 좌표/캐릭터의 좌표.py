def solution(keyinput, board):
    x,y=0,0
    maxx = (board[0]) //2
    minx = -maxx
    maxy = (board[1]) //2
    miny = -maxy
    
    for i in keyinput:
        if i == 'up':
            if y<maxy:
                y+=1
        elif i == 'down':
            if y>miny:
                y -= 1
        elif i == 'left':
            if x>minx:
                x -= 1
        elif i == 'right':
            if x<maxx:
                x += 1
    return [x,y]