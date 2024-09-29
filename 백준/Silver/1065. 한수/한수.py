def hansu(n):
    digits = list(map(int, str(n)))
    if n < 100:
        return True
    else:
        diff = digits[1] - digits[0]
        for i in range(1, len(digits) - 1):
            if digits[i+1] - digits[i] != diff:
                return False
        return True
    
n = int(input())
count = 0
for i in range(1, n + 1):
    if hansu(i):
        count += 1

print(count)