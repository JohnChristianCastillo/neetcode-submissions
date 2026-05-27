class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        1. use hashmap s.t.: hask[key] = [index]
        2. loop over nums
        - calculate difference
        - check if difference in hashmap
        - yes: return curr index + diff index
        - no: move next
        """

        mp = defaultdict(list)
        for i in range(len(nums)):
            mp[nums[i]].append(i)
        
        for i in range(len(nums)):
            curr = nums[i]
            diff = target - curr
            if diff in mp:
                # possible diff = same as curr
                # say tar = 6, curr = 3, diff = 3
                # but there's only one 3
                if diff == curr:
                    if len(mp[diff]) >= 2:
                        return mp[diff][0:2] # return first 2 elements
                else: # not same AND we know it's in MP
                    return [i, mp[diff][0]] # still possible there's a duplicate
                    # say tar = 7, curr = 4, diff = 3, nums = [3,3,3,3]
        
