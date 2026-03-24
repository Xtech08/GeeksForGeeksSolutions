#You are given an integer array arr[]. You need to find the maximum sum of a subarray (containing at least one element) in the array arr[].

def maxSubarraySum(self, arr):
        arr1=[]
        s=0
        for i in range(len(arr)):
            s+=arr[i]
            arr1.append(s)
        M=[]
        M.append(max(arr1))
        for i in range(len(arr1)):
            if arr1[i]<0 and i+1<len(arr1):
                M.append(max(arr1[i+1:len(arr1)])-arr1[i])
        return max(M)
