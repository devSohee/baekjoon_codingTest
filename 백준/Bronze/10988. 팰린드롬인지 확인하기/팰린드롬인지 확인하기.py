import sys
s=input()
for i in range(int(len(s)/2)):
    if s[i] != s[-i-1]:
        print(0)
        sys.exit()
print(1)