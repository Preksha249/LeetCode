class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums) - 1
        list = []
        nums.sort()
        for i in range(n):
            if i>0 and nums[i] == nums[i -1]:
                continue

            l = i+1
            k = n
            while l < k:
                sum = nums[i]+nums[l]+nums[k]
                if sum > 0:
                    k -=1
                elif sum < 0:
                    l+=1
                else:
                    list.append([nums[i],nums[l],nums[k]])
                    l+=1
                    while nums[l] == nums[l-1] and l<k:
                        l+=1
        return list