s=input()
n=int(input())
l=input().upper()
k=''
if n==len(s):
    print(str(s))
else:
    if l=='L':
        for i in range(n):
            k=s[0]
            s=s[1:len(s)]
            s=s+k
    else:
        for i in range(n):
            k=s[len(s)-1]
            s=k+s[:len(s)-1]
    print(s)