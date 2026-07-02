def nu(i,n):
    if i==n:
        print(i)
        return
    print(i)
    return nu(i+1,n)
n=int(input())
nu(1,n)