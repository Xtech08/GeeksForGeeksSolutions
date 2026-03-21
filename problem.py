#You are given an integer array 𝑎
# of length 𝑛
.

#For each index 𝑖
, find the maximum number of indices 𝑗
 such that 𝑗>𝑖
# and |𝑎𝑖−𝑘|>|𝑎𝑗−𝑘|
, over all possible integer values of 𝑘

def P(L):
    L1={}
    L2={}
    for i in range(0,len(L)):
        L1[f"{i}"]=[]
        L2[f"{i}"]=[]
        for j in range(i+1,len(L)):
            if L[j]>L[i]:
                L1[f"{i}"].append(L[j])
            else:
                L2[f"{i}"].append(L[j])
    
    L3=[]
    for i in range (len(L)):
        if len(L1[f"{i}"])>len(L2[f"{i}"]):
            L3.append(len(L1[f"{i}"]))
        else:
            L3.append(len(L2[f"{i}"]))
    return L3
print(P([9,18,29817,283,3,3928,5726,1942,1000000000,-1000000000,19]))
