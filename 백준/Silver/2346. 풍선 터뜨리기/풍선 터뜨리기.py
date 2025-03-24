from collections import deque
import sys
N = int(input())
dq = deque()
balloons = deque()
for _ in range(1, N + 1):
    balloons.append(_)
for i in sys.stdin.readline().rstrip().split():
    dq.append(int(i))

stk = []
stk.append(balloons.popleft())
idx = dq.popleft()
while dq:
    if idx > 0:
        for _ in range(1, idx):
            balloons.append(balloons.popleft())
            dq.append(dq.popleft())
        stk.append(balloons.popleft())
        idx = dq.popleft()
    else:
        for _ in range(1, abs(idx)):
            balloons.appendleft(balloons.pop())
            dq.appendleft(dq.pop())
        stk.append(balloons.pop())
        idx = dq.pop()
        
print(*stk)