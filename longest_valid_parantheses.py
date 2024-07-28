# 32. Longest Valid Parentheses

# Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring

# Example 1:
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".

# Example 2:
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".

# Example 3:
# Input: s = ""
# Output: 0
 
# Constraints:
# 0 <= s.length <= 3 * 104
# s[i] is '(', or ')'.

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # now lets define a variable max length to keep a track of valid parantheses
        max_len = 0
        # now lets define a stack with value -1 so as to handle edge case where the valid parantheses is found at the beginning of the stack
        stack = [-1]

        # now we need to check the character along with the index
        for i,c in range(len(s)):
            # if we find open parantheses we append it at the position i
            if c == "(" :
                stack.append(i)
            # if not open parantheses we pop it
            else:
                stack.pop()
                # now if there is no matching parantheses for open to close/ stack is empty then we will append it
                if not stack:
                    stack.append(i)
                # if stack is not empty then we find out max length between current valid substring and previous max_len
                else:
                    max_len = max(max_len, i - stack[-1])
                
        return max_len