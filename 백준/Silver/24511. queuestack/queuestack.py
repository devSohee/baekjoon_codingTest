from collections import deque as dq
import sys
input = sys.stdin.readline
N = int(input().rstrip())
qs = list(map(int, input().rstrip().split()))
sqF = list(map(int, input().rstrip().split()))
sq = dq()
for i in range(N):
    if qs[i] == 0:
        sq.append(sqF[i])

M = int(input().rstrip())
result = []
for d in list(map(int, input().rstrip().split())):
    sq.appendleft(d)
    result.append(sq.pop())

print(*result)