'''Therer is a range given n and m in which we have to find the count all the prime pairs whose difference is 6.  we have to find how many sets are thre within a given
range.
'''

def pr(i):
    for j in range(2,i//2 +1):
        if i%j==0:
            return False
        else:
            continue
    return True
m,n=map(int,input().split())
cnt=0
a=[]
for i in range(m,n+1):
    if pr(i):
        a.append(i)
for i in range(len(a)):
    for j in range(i,len(a)):
        if a[j]-a[i]==6:
            print(a[j],a[i])
            cnt+=1
print(cnt)
'''
def pr(a):
    for j in range(2,a//2 +1):
        if i%j==0:
            return False
        else:
            continue
    return True

m,n=map(int,input().split())
cnt=0
for i in range(m,n-5):
    if pr(i) and pr(i+6):
        print(i,i+6)
        cnt+=1
print(cnt)
'''