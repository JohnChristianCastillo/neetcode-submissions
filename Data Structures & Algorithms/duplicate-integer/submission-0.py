class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m = defaultdict()
        for v in nums:
            if v in m:
                return True
            else:
                m[v] = 1
        return False