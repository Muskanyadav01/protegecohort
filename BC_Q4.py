class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        length=len(nums1)
        count=0
        for i in range(len(nums1)):
            if nums1[i]==0:
                count=count+1
        while count>=1:
            nums1.pop()
            count=count-1
        num3=nums1+nums2
        print(sorted(num3))
