#Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.



def Sort012(arr):
    C0=0
    C1=0
    for i in range(0,len(arr)):
        if arr[i]==0:
            C0+=1
        elif arr[i]==1:
            C1+=1
    A1=[0 for x in range(0,C0)]
    A2=[1 for x in range (0,C1)]
    A3=[2 for x in range (0,len(arr)-C0-C1)]
    A1.extend(A2)
    A1.extend(A3)
    return A1
  
