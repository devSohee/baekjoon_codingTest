n=0
input()
s=input()
while s:
    n+=int(s[-1])
    s=s[:-1]
print(n)