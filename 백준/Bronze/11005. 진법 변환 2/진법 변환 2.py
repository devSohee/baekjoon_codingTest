from collections import deque as dq
r=dq()
N,B=list(map(int,input().split()))
while N:
    m=N%B
    if m < 10: r.appendleft(str(m))
    else: r.appendleft(chr(m+55))
    N//=B
print(''.join(list(r)))