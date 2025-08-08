class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        current = 0

        for n in nums:
            if current < 0 :
                current = 0
            current += n
            maxSub = max(maxSub, current)
        return maxSub
