n=int(input())
while n != -1:
    r=set()
    for i in range(1, int(n**(1/2)) + 1):
        if n % i == 0:
            r.add(i)
            r.add(n//i)
    r=sorted(list(r))
    if sum(r[:-1]) == n: print(f'{n} = {' + '.join(list(map(lambda x: str(x),r[:-1])))}')
    else: print(f'{n} is NOT perfect.')
    n=int(input())