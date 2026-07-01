'''def ug(i):
    while(i%2==0 or i%3==0 or i%5==0):
        if i%2==0:
            i//=2
        elif i%3==0:
            i//=3
        elif i%5==0:
            i//=5
    if i==1:
        return True
    else:
        return False


n=int(input())
cnt=1
i=1
while cnt<=n:
    if ug(i):
        cnt+=1
        print(i,end=" ")
    i+=1
print()
print(i-1)'''

def md(i,b):
    while i%b==0:
        i=i//b
    return i

def ug(i):
    i=md(i,2)
    i=md(i,3)
    i=md(i,5)

    if i==1:
        return True
    else:
        return False

n=int(input())
cnt=1
i=1
while cnt<=n:
    if ug(i):
        cnt+=1
        print(i,end=" ")
    i+=1
print()
print(i-1)