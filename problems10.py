
def allSum(nums):
    n=len(nums)
    if n==0: return 0
    if n==1: return nums[0]
    if n < 4: return max(nums)
    sum1=0
    sum2=0
    for i in range(0,n):
        if i %2 ==0:
            sum1 += nums[i]
        else:
            sum2 += nums[i]
    return max(sum1,sum2)

def arrSum(nums):
    all_sum=[]
    for i in range(len(nums)):
        all_sum.append(allSum(nums[i:]))
    return max(all_sum)

print(arrSum([1,-2,3,4,-5,6,-7,8,9]))

def myallSum(nums):
    n=len(nums)
    if n==0: return 0
    if n==1: return nums[0]
    if n < 4: return max(nums)
    first_sum=0
    second_sum=0
    for i in range(0,n):
        if i %2 ==0:
            first_sum =max(nums[i]+first_sum,first_sum)
        else:
            second_sum=max(nums[i]+second_sum,second_sum)
    return max(first_sum,second_sum)

print(myallSum([1,-2,3,4,-5,6,-7,8,9]))