n,k=map(int, input().split())
r=set()
for i in range(1, int(n**(1/2)) + 1):
    if n % i == 0:
        r.add(i)
        r.add(n//i)
r=sorted(list(r))
print(r[k-1] if k <= len(r) else 0)