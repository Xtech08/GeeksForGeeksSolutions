#FindingMaxAndMinFromAnArray
def findMax(nums):
    if len(nums)==1:
        return nums[0]
    elif len(nums)==0:
        return []
    elif findMax(nums[0:len(nums)//2]) < findMax(nums[len(nums)//2:len(nums)]):
        return findMax(nums[len(nums)//2:len(nums)])
    else :
        return findMax(nums[0:len(nums)//2])
def findMin(nums):
    if len(nums)==1:
        return nums[0]
    elif len(nums)==0:
        return []
    elif findMin(nums[0:len(nums)//2]) < findMin(nums[len(nums)//2:len(nums)]):
        return findMin(nums[0:len(nums)//2])
    else :
        return findMin(nums[len(nums)//2:len(nums)])
def findMinandMax(nums):
    print(f"Max={findMax(nums)}\nMin={findMin(nums)}")
