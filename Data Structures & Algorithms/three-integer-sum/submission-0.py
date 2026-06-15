class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        !! use seen set to remember all ANCHOR POINTS we've seen
        sort nums --> to know how many we have of each element
        loop over nums
        -> use 3 pointers, with:
            - a: anchor
            - l: next element
            - r: rightmost element
        -> perform collapsing window search (collapse l,r)
           to find a + l + r  s.t.  sum == 0
        """
        nums.sort()
        seen = set()
        sols = []
        for i, v in enumerate(nums):
            if i in seen:
                continue
            seen.add(i)
            lo, hi = i + 1, len(nums)-1
            while lo < hi:
                curr_sum = v + nums[lo] + nums[hi]
                if curr_sum == 0:
                    sol = [nums[i], nums[lo], nums[hi]]
                    if sol not in sols:
                        sols.append(sol)
                    lo += 1
                elif curr_sum < 0:
                    lo += 1
                else:
                    hi -= 1
        return sols