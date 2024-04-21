def solution(arr):
    row = len(arr)
    cols = len(arr[0]) if arr else 0
    
    if row > cols:
        for i in arr:
            i.extend([0] *(row-cols))
    
    
    elif cols > row:
        for _ in range(cols -row):
            arr.append([0] *cols)
    return arr