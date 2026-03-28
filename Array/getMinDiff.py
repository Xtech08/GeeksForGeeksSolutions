# Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.

def getMinDiff(arr, k):
    arr.sort()
    m0=arr[0]
    M0=arr[len(arr)-1]
    smallest=M0-m0
    for i in range(1,len(arr)):
        if arr[i]-k<0:
            continue
        m=min(m0+k,arr[i]-k)
        M=max(M0-k,arr[i-1]+k)
        smallest=min(smallest,M-m)
    return smallest
