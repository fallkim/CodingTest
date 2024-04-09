def solution(slice, n):
    total_pizzas = n // slice + (1 if n % slice != 0 else 0)
    return total_pizzas