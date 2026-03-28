#You are given an array arr[] of non-negative numbers. Each number tells you the maximum number of steps you can jump forward from that position.

For example:

If arr[i] = 3, you can jump to index i + 1, i + 2, or i + 3 from position i.
If arr[i] = 0, you cannot jump forward from that position.
Your task is to find the minimum number of jumps needed to move from the first position in the array to the last position.

Note:  Return -1 if you can't reach the end of the array.



def minJumps(self, arr):
	    D={}
	    if len(arr)==1:
            return 0
        if len(arr)==0:
            return 0
	    t=arr[0]
	    if t==0:
	        return -1
	    if t==1:
	        if self.minJumps(arr[1:])==-1:
	            return -1
	        return self.minJumps(arr[1:])+1
	    else:
	        s=len(arr)
	        k=0
	        for j in range(1,arr[0]+1):
	            if self.minJumps(arr[j:])==-1:
	                continue
	            else:
	                k=1
	                s=min( self.minJumps(arr[j:])+1,s)
	        if k==0:
	            return -1
	        return s
