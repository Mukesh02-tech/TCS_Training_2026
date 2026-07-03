def mo(a,b,c,r):
    if c>a or r>b:
        return 0
    if a==c and b==r:
        return 1
    return mo(a,b,c+1,r)+mo(a,b,c,r+1)

a,b=map(int,input().split())
print(mo(a-1,b-1,0,0))
