n=[[] for _ in range(9)]
mi,mj=0,0
for i in range(9):
    n[i]=(list(map(int,input().split())))
    if n[mi][mj] < max(n[i]): 
        mi = i
        mj = n[i].index(max(n[i]))
print(n[mi][mj])
print(mi+1,mj+1)