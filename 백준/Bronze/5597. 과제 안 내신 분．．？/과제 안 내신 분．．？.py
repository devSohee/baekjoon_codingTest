s=[0 for _ in range(30)]
for _ in range(28):
    s[int(input())-1]=1
print(s.index(0)+1)
s.remove(0)
print(s.index(0)+2)