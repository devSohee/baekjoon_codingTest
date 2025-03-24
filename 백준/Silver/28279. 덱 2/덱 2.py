from collections import deque
import sys
dq = deque()
for _ in range(int(input())):
    cmd = sys.stdin.readline().rstrip().split()
    match int(cmd[0]):
        case 1:
            dq.appendleft(cmd[-1])
        case 2:
            dq.append(cmd[-1])
        case 3:
            print(dq.popleft() if dq else -1)
        case 4:
            print(dq.pop() if dq else -1)
        case 5:
            print(len(dq))
        case 6:
            print(0 if dq else 1)
        case 7:
            print(dq[0] if dq else -1)
        case 8:
            print(dq[-1] if dq else -1)