# 1929. Concatenation of Array
# Specifically, ans is the concatenation of two nums arrays.

# Return the array ans.

 # Example 1:

# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]

# Example 2:

# Input: nums = [1,3,2,1]
# Output: [1,3,2,1,1,3,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
# - ans = [1,3,2,1,1,3,2,1]

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # lets define an array in which we wish to store the new array
        ans = []

        # now as we can see we need to append and since these are the same values we need to do it twice

        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# now even if we were asked to concat it 3 or maybe 4 or 5 times we just need to change the value in the first for loop 
# or even if we were given a user defined value say 'x' then the following changes are to be applied

class Solution:
    def getConcatenation(self, nums: List[int], x) -> List[int]:
        # lets define an array in which we wish to store the new array
        ans = []

        # now as we can see we need to append and since these are the same values we need to do it twice

        for i in range(x):
            for n in nums:
                ans.append(n)
        return ans

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------


                