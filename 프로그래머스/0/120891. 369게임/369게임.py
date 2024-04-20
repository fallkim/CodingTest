def solution(order):
    count = 0
    order_str = str(order)
    for i in order_str:
        if i in '369':
            count +=1
    return count