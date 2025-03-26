s=[]
c=[]
for l in input():
    t=l.upper()
    if t in s:c[s.index(t)]+=1
    else:
        s.append(t)
        c.append(1)
if c.count(max(c))>1:print('?')
else:print(s[c.index(max(c))])