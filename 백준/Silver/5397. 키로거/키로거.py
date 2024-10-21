def find_password(words):
    left_stack = []
    right_stack = []

    for char in words:
        if char == '-':
            if left_stack:
                left_stack.pop()
        elif char == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif char == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(char)
    
    return ''.join(left_stack) + ''.join(reversed(right_stack))

test = int(input())

for _ in range(test):
    words = input().strip()
    print(find_password(words))