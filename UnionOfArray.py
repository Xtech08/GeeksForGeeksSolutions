#You are given two arrays a[] and b[], return the Union of both the arrays in any order.

def findUnion( a, b):
        L=[]
        for i in range(len(a)):
            if a[i] not in L:
                L.append(a[i])
        for i in range(len(b)):
            if b[i] not in L:
                L.append(b[i])
        return L
