

'''
#not completed fully
t=int(input())
for i in range(t):
    n=int(input())
    while n%10==0 or n%20==0:
        if n%20==0 and (n//10)%10!=0:
            n//=20
        elif n%10==0:
            n//=10
    if n==1:
        print("Yes")
    else:
        print("No")
'''

def hack(n,i):
    if n==i:
        return True
    if i>n:
        return False
    else:
        if hack(n,i*10):
            return True
        if hack(n,i*20):
            return True
    return False


t=int(input())
for i in range(t):
    n=int(input())
    print(hack(n,1))