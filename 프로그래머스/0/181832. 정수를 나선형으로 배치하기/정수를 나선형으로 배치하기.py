def solution(n):
    rr = [[0] * n for _ in range(n)]
    
    x,y =0,0
    dx, dy = 0,1
    num = 1
    while num <= n*n:
        rr[x][y] = num
        num+=1
        
        nx,ny = x+dx, y +dy
        
        if nx < 0 or nx >= n or ny < 0 or ny >= n or rr[nx][ny] != 0:
            # 방향 전환: 오른쪽 -> 아래 -> 왼쪽 -> 위
            if dx == 0 and dy == 1:
                dx, dy = 1, 0
            elif dx == 1 and dy == 0:
                dx, dy = 0, -1
            elif dx == 0 and dy == -1:
                dx, dy = -1, 0
            elif dx == -1 and dy == 0:
                dx, dy = 0, 1
            nx, ny = x + dx, y + dy
        
        # 다음 위치로 이동
        x, y = nx, ny
    return rr