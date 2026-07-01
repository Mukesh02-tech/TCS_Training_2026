def re(a):
    k=[]
    m=a.index(min(a[0],a[len(a)-1]))
    if m==0:
        k.append(a[0]+a[1])
        for i in range(2,len(a)):
            k.append(a[i])
        return k
    else:
        k=a[:len(a)-2]
        k.append(a[m-1]+a[m])
        return k

t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=a[::-1]
    cnt=0
    while a!=b:
        cnt+=1
        a=re(a)
        b=a[::-1]
        print(a)
    print(cnt)