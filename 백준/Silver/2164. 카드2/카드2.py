from collections import deque

dq = deque()

for _ in range(int(input())):
    dq.append(_ + 1)

while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq.pop())