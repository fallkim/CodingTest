from collections import deque

def fast_time(n,k):
    if n >= k :
        return n - k

    max_pos = 100000
    visited = [-1] * (max_pos + 1)
    queue = deque([n])
    visited[n] = 0

    while queue:
        current = queue.popleft()

        for next_pos in (current -1, current +1, current * 2):
            if 0 <= next_pos <= max_pos and visited[next_pos] == -1:
                visited[next_pos] = visited[current] + 1
                queue.append(next_pos)
                if next_pos == k:
                    return visited[next_pos]
    return visited[k]

n,k = map(int,input().split())
print(fast_time(n,k))