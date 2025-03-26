g={'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0,'P':0}
a=0
c=0
for _ in range(20):
    s=list(input().split())
    if s[-1]!='P':
        c+=float(s[1])
        a+=g[s[2]]*float(s[1])
print('%.6f'%(a/c))