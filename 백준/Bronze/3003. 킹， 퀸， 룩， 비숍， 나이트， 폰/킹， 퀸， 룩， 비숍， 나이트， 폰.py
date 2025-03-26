c=[1,1,2,2,2,8]
h=list(map(int,input().split()))
for i in range(6):c[i]-=h[i]
print(*c)