class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr1 = m - 1
        ptr2 = n - 1

        for merge_index in range(m + n - 1, -1, -1):
            if ptr2 < 0:
                return 
            
            if nums1[ptr1] >= nums2[ptr2] and ptr1 >= 0:
                nums1[ptr1], nums1[merge_index] = nums1[merge_index], nums1[ptr1]
                ptr1 -= 1
            
            else:
                nums2[ptr2], nums1[merge_index] = nums1[merge_index], nums2[ptr2]
                ptr2 -= 1
        

