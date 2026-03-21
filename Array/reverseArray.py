#reverse an array without using builtin function

def reverseArray(nums):
    for i in range(0,(len(nums))//2):
        nums[i],nums[-i-1]=nums[-i-1],nums[i]
    print(nums)
