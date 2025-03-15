N,K = map(int,input().split())
coins = [int(input()) for _ in range(N)]
cnt = 0
for i in range(1, N+1):
    if coins[-i] <= K:
        cnt += K // coins[-i]
        K = K % coins[-i]
        if K == 0: break
print(cnt)