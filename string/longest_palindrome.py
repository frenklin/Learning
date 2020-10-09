#!/usr/bin/env python
#Based on https://articles.leetcode.com/longest-palindromic-substring-part-ii/
# Manchester algo
# O(N)


def format(s):
    for c in s:
      yield "#"
      yield c
    yield "#"

def clear(s):
    for c in s:
      if c != "#":
        yield c


def longestPalindrome(s):
  s = list(format(s))
  C = 0
  R = 0
  P = [0]*len(s)
  for i in range(1, len(s)-1):
    i_mirror = 2*C - i
    P[i] = min(R-i, P[i_mirror]) if R > i else 0

    # Attempt to expand palindrome centered at i
    while i + 1 + P[i]<len(s) and i - 1 - P[i]<len(s) and s[i + 1 + P[i]] == s[i - 1 - P[i]]:
      P[i] = P[i]+1

    # If palindrome centered at i expand past R,
    # adjust center based on expanded palindrome.
    if (i + P[i] > R):
      C = i
      R = i + P[i]

  # Find the maximum element in P.
  maxLen = 0
  centerIndex = 0
  for i in range(1, len(s)-1):
    if P[i] > maxLen:
      maxLen = P[i]
      centerIndex = i
  return "".join(clear(s[centerIndex-maxLen:centerIndex])) + "".join(clear(s[centerIndex:centerIndex+maxLen]))


print(longestPalindrome("badaoadm"))
