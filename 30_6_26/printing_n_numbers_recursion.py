def pr(n):
    if n==1:
        print(n)
    else:
        print(n,end=" ")
        pr(n-1)

n=int(input())
pr(n)