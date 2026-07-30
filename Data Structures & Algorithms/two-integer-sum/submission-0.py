class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            differance = target - num
            if differance in hash_map:
                return [hash_map[differance], i]
            hash_map[num] = i