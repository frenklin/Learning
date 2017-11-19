#!/usr/bin/env python

""""""
MAX_VALUE = 1000000000

def kthElement(A, startA, B, startB, k):
    if len(A)-1 < startA:
        return B[startB+k-1]
    if len(B)-1 < startB:
        return A[startA+k-1]
    if k==1: 
        return min(A[startA], B[startB])
    
    midA=A[startA+k//2-1] if startA+k//2-1 < len(A) else MAX_VALUE;
    midB=B[startB+k//2-1] if startB+k//2-1 < len(B) else MAX_VALUE;
    
    if midA<midB:
        return kthElement(A, startA+k//2, B, startB, k-k//2)
    else:
        return kthElement(A, startA, B, startB+k//2, k-k//2)
        
def med(arr1, arr2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """            
    n=len(arr1)
    m=len(arr2)
    l=(m+n+1)//2
    r=(m+n+2)//2
    return (kthElement(arr1,0,arr2,0,l)+kthElement(arr1,0,arr2,0,r))/2.0      


ar1 = [1,2]
ar2 = [3,4]

print(med(ar1, ar2))
