#given 2 sorted arrays of different sizes, return the median of the two arrays (without merging)
#time complexity: Olog(n). SEE NOTEBOOK FOR EXPLANATION

def findMedianSortedArrays(nums1, nums2):
    A,B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2
    if len(A) > len(B):
        A,B = B,A
    l,r = 0, len(A)-1
    while True:
        
    