# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false
 

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        # lets define the stack
        stack = []
        # now we can define the dictionary so that we can map the closing paratheses to opening parantheses
        closeToOpen = {")" : "()", "]" : "[", "}" : "{"}

        # now we want to iterate through each character in the input string 
        for c in s:
            # now we have to check if the character is in the dictionary
            if c in closeToOpen:
                # now we have to check if the is not empty and last/top element is the corresponding one for the element we first read
                if stack and stack[-1] == closeToOpen[c]:
                    # if it matches then we pop that element
                    stack.pop()
                else:
                    return False
            # now if c is opening bracket and not found in the dictionary
            else:
                stack.append()

        # now we have to check after popping if the stack is empty or not 
        # if empty we return True and if not we return False
        return True if not stack else False


