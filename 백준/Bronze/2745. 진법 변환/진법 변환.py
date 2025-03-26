r=0
N,B=input().split()
for i in range(len(N)):
    t=int(N[-i-1]) if N[-i-1].isnumeric() else ord(N[-i-1])-55
    r+=int(B)**i*t
print(r)