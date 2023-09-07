class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Approach 1
        # for j in range(n):
        #     nums1[m] = nums2[j]
        #     m += 1

        # nums1.sort()

        # Approach 2: Merge from the tail
        t = m + n - 1

        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[t] = nums1[m - 1]
                m -= 1
            else:
                nums1[t] = nums2[n - 1]
                n -= 1

            t -= 1

        # use leftovers in nums2, if any
        while n > 0:
            nums1[t] = nums2[n - 1]
            n -= 1
            t -= 1
