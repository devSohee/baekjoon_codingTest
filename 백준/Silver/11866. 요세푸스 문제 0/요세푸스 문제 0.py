from collections import deque

N, K = map(int, input().split())

dq = deque()
Josephus = deque()
for _ in range(1, N + 1):
    dq.append(_)
idx = 1
while dq:
    if idx == K:
        Josephus.append(dq.popleft())
        idx = 1
    else:
        dq.append(dq.popleft())
        idx += 1
print("<" + ", ".join(map(str, Josephus)) + ">")