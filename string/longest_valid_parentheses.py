#!/usr/bin/env python
# O(n)

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """       
        max_len = 0
        stack = [-1]
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len


s = Solution()
assert(s.longestValidParentheses("))())()()(()") == 4)
assert(s.longestValidParentheses("()()(()()") ==  4 )
assert(s.longestValidParentheses(")()())()()(") ==  4)
assert(s.longestValidParentheses(")())()()(()") == 4)

assert(s.longestValidParentheses("))))())()()(()") == 4)
assert(s.longestValidParentheses(")(") ==  0 )
assert(s.longestValidParentheses("())()") == 2)
assert(s.longestValidParentheses("()()(") == 4)
assert(s.longestValidParentheses("()") == 2)
assert(s.longestValidParentheses("())") == 2)
assert(s.longestValidParentheses(")()") == 2)
assert(s.longestValidParentheses(")(())))(())())") == 6)
assert(s.longestValidParentheses(")()(((())))(") ==  10 )

assert(s.longestValidParentheses('()()') == 4 )
assert(s.longestValidParentheses('()())') == 4 )
assert(s.longestValidParentheses('(()()') == 4 )
assert(s.longestValidParentheses('(()') == 2 )
assert(s.longestValidParentheses('(())') == 4 )