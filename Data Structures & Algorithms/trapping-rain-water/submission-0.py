class Solution:
    def trap(self, height: List[int]) -> int:
        """
        use 2 pointers initialized at beginning and end
        use the lower of the two as the supremum to calculate water
        """
        l, r = 0, len(height)-1
        lb, rb = height[l], height[r]
        total_water = 0
        while l < r:
            if lb < rb:
                # lb is supremum
                total_water += lb - height[l]
                # move pointer
                l += 1
                # update lb if needed
                lb = max(lb, height[l])

            else:  
                total_water += rb - height[r]
                r -= 1 # move to next 
                # see if we need to update r
                rb = max(rb, height[r])

        return total_water