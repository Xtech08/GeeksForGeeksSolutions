#Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

def findDuplicate( nums: List[int]) -> int:
        D=[0 for i in range (len(nums))]
        for i in range(len(nums)):
            D[nums[i]]=D[nums[i]]+1
        for i in range(len(D)):
            if D[i]>=2:
                return i
