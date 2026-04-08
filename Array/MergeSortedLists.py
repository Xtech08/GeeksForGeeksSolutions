#Merge two sorted lists without extra space.



def MergeSortedLists(L1,L2):
    L=[]
    for i in range(0,len(L1)+len(L2)-1):
        if L1[0]<L2[0]:
            L.append(L1[0])
            L1.pop(0)
            if len(L1)==0:
                L.extend(L2)
                return L
        else:
            L.append(L2[0])
            L2.pop(0)
            if len(L2)==0:
                L.extend(L1)
                return L
