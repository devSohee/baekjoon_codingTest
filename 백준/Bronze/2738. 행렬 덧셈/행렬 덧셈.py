N,M=map(int,input().split())
m = [[0]*M for _ in range(N)]
for k in range(2):
    for i in range(N):
        n=list(map(int,input().split()))
        m[i] = [m[i][j] + n[j] for j in range(M)]

for i in range(N):
    print(*m[i])