#!/usr/bin/env python
import collections

class Solution(object):

    def ladderLength(self, beginWord, endWord, wordList):
        
        def construct_dict(wordList):
            ret = collections.defaultdict(list)
            for word in wordList:
                for i in range(len(word)):
                    blank = word[:i] + '_' + word[i + 1:]                    
                    ret[blank].append(word)
            return ret
        
        def bfs(beginWord, endWord, wordDict):
            queue, visited = [(beginWord, 1)], set()
            while queue:
                word, step = queue.pop(0)
                if word not in visited:
                    visited.add(word)
                    if word == endWord:
                        print(word)
                        return step
                    for i in range(len(word)):
                        blank = word[:i] + '_' + word[i + 1:]
                        neighbors = wordDict[blank]
                        for neighbor in neighbors:
                            if neighbor not in visited:
                                queue.append((neighbor, step + 1))
            return 0
        wordDict = construct_dict(wordList)
        return bfs(beginWord, endWord, wordDict)
    



beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

s = Solution()

print(s.ladderLength(beginWord, endWord, wordList))