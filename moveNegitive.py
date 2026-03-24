Given an array containing both positive and negative numbers in random order. The task is to rearrange the array elements so that all negative numbers appear before all positive numbers.
def MoveNeg(lis):
    L1=[]
    L2=[]
    for i in range (len(lis)):
        if lis[i]<0:
            L1.append(lis[i])
        else:
            L2.append(lis[i])
    L1.extend(L2)
    return L1
