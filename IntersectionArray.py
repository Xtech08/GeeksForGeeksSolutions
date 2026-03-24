#Given array a, b returns intersection set,(every element can belong to intersection only once,or cannot belong to intersection)
def Intersection(a,b):
    L1=[]
    L2=[]
    for i in range(len(a)):
        if a[i] not in L1:
            L1.append(a[i])
    for i in range(len(b)):
        if b[i] not in L2:
            L2.append(b[i])
    L1.extend(L2)
    L=[]
    while i<len(L1):
        x=L1[i]
        L1.pop(i)
        if x in L1:
            L.append(x)
        if i==len(L1):
            break
    return L
  
