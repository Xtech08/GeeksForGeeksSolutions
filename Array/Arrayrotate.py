#Given an array arr, rotate the array by one position in clockwise direction.

def rotate(self, arr):
        for i in range(1,len(arr)):
            arr[-i],arr[-i-1]=arr[-i-1],arr[-i]
        return arr
