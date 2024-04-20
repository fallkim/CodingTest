def solution(date1, date2):
    tuple_date1 = tuple(date1)
    tuple_date2 = tuple(date2)
    if tuple_date1 < tuple_date2:
        return 1
    return 0