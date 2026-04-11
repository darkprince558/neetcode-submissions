class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1, 0, -1 ):
            n = target - nums[i]
            if n in nums:
                return[nums.index(n), i]        