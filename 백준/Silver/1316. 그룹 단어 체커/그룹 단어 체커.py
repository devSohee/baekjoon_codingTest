r=0
for _ in range(int(input())):
    s=input()
    g=[s[0]]
    b=True
    for c in s[1:]:
        if c in g:
            if c != g[-1]:
                b=False
                break
        else:g.append(c)
    if b:r+=1
print(r)