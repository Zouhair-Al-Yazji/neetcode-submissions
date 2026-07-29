class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqe_nums = set()
        for num in nums:
            if num in uniqe_nums:
                return True
            uniqe_nums.add(num)
        return False