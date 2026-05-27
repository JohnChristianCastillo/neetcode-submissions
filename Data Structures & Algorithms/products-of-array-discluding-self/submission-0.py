class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        1. find total product excluding all 0's
        2. find amount of zero's
            if more than 1 zero: return array of 0's
        3. loop over nums:
            if nums[i] == 0:
                just the total product
            else: # not zero 
                # remember we already returned if more than 1 zero
                # so only case left is if there is atleast 1 zero
                  in that case we make nums[i] = 0
        """

        zeros = 0
        prod = 1
        for v in nums:
            if not v:
                zeros += 1
            else:
                prod *= v
        
        if zeros > 1:
            return [0]*len(nums)

        for i, v in enumerate(nums):
            if v == 0:
                nums[i] = prod
            else:
                if zeros:
                    nums[i] = 0
                else:
                    nums[i] = prod//nums[i]
        return nums
            
                