# 75. Sort Colors

# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

#Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # first we will define the left and the right pointer and set the left to 0 and right to the last index of array
        left, right = 0, len(nums) -1
        # now we will use a variable for traversing
        i = 0
        # now we will run the loop till the end 
        while i <= r:
            # handling 0's
            if nums[i] == 0:
                # if we come across 0 value we swap it with left position
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
            # handling 2's
            elif nums[i] == 2:
                # if we come across 2 then we swap with right position
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
                # we would also decrement i counter for handling 2's
                i -= 1
            # but when we come out then we need to increment it
            i += 1