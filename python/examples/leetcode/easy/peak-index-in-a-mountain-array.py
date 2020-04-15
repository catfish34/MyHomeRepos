class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        lo, hi = 0, len(A) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if A[mid] < A[mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        return lo


ans = Solution().peakIndexInMountainArray([1, 2, 3, 4, 1])
print(ans)