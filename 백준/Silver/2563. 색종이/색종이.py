N=int(input())
c=[]
maxx,maxy,r=0,0,0
for i in range(N):
    c.append(list(map(int,input().split())))
    maxx=maxx if maxx > c[i][0] else c[i][0]
    maxy=maxy if maxy > c[i][1] else c[i][1]
m=[[0 for _ in range(maxx+10)] for _ in range(maxy+10)]
for b in c:
    for i in range(b[0]-1,b[0]+9):
        for j in range(b[1]-1,b[1]+9):
            m[j][i]=1
for i in m:r+=i.count(1)
print(r)