def pr(i):
    for j in range(2,i//2+1):
        if i%j==0:
            return False
    return True
def cn(n):
    a=n-1
    b=n+1
    while True:
        if pr(a):
            return a
        if pr(b):
            return b
        if a>1:
            a-=1
        b+=1
n=int(input())
print(cn(n))