#Given an integer array arr[] and an integer k, your task is to find and return the kth smallest element in the given array.


def kthSmallest(arr, k):
        def Sort2array(arr1,arr2,a=[]):
            if arr1==[]:
                a.extend(arr2)
                return a
            elif arr2==[]:
                a.extend(arr1)
                return a
            elif arr1[0]>arr2[0]:
                a.append(arr2[0])
                arr2.pop(0)
                
                return Sort2array(arr1,arr2,a)
            else:
                a.append(arr1[0])
                arr1.pop(0)
                
                return Sort2array(arr1,arr2,a)
        def sort(arr):
            if len(arr)==0 or len(arr)==1:
                return arr
            A1=arr[0:len(arr)//2]
            A2=arr[len(arr)//2:len(arr)]
            return Sort2array(sort(A1),sort(A2),[])
        Z={}
        if f"{arr}" not in Z:
        Z[f"{arr}"]=sort(arr)
        return Z[f"{arr}"][k-1]
    
