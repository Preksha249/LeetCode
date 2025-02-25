class Solution:
    #Preksha
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        n= len(nums)
        for i in range(n-1):
            for k in range(i+1, n):
                if(nums[i]+nums[k] == target):
                    return i,k

                
        