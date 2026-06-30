'''
To find the unique digits from the given range of numbers
input:10 15
output: 5
input2: 109 123
output2: 3
'''
'''def se(i,cnt):
    n=[]
    while i>0:
        if i%10 in n:
            return cnt
        else:
            n.append(i%10)
            i//=10
    return cnt+1
a,b=map(int,input().split())
cnt=0
for i in range(a,b+1):
    cnt=se(i,cnt)
print(cnt)'''

def ln(i):
    n=[]*10
    while i!=0:
        n[i%10]+=1
        i//=10
    for j in n:
        if j>1:
            return False
    return True