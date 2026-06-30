def thirdMax(nums):
    nums=sorted(list(set(nums)))
    if len(nums)>2:
        return nums[-3]
    else:
        return nums[-1]
        
nums=list(map(int,input().split()))
print(thirdMax(nums))