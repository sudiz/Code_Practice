class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:m+n]=nums2
        i=m-1
        j=m+n-1
        while i>=0 and j>i:
            if nums1[i]>=nums1[j]:
                nums1[i:j],nums1[j]=nums1[i+1:j+1],nums1[i]
                i-=1
                j-=1
            else:
                j-=1
            
