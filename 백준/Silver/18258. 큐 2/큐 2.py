from collections import deque
import sys
dq = deque()
for _ in range(int(input())):
    cmd = sys.stdin.readline().rstrip().split()
    match cmd[0]:
        case 'push':
            dq.append(int(cmd[1]))
        case 'pop':
            print(dq.popleft() if dq else -1)
        case 'size':
            print(len(dq))
        case 'empty':
            print(0 if dq else 1)
        case 'front':
            print(dq[0] if dq else -1)
        case 'back':
            print(dq[-1] if dq else -1)