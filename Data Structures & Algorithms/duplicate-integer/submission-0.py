class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums:
            n = {}
            for i in nums:
                if i in n:
                    return True
                n[i] = 5
        return False

