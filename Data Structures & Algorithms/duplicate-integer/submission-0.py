class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        match = []
        for num in nums:
            if num in match:
                return True
            else:
                match.append(num)
        
        return False
        