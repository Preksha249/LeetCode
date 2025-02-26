class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, n = 0, len(numbers)-1
        list = []
        while l<n:
            sum = numbers[l]+numbers[n]

            if sum > target:
                n -=1
            elif sum < target:
                l+=1
            else:
                return [l+1,n+1]
            
            
        return list
        
        
        