def sub(n,i,a):
    if i==len(n):
        print(a)
        return
    a.append(n[i])
    sub(n,i+1,a)
    a.pop()
    sub(n,i+1,a)

n=list(map(int,input().split()))
sub(n,0,[])