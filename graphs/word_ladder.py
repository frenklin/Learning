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


''' class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        wordDict = set(wordList)
        length = 2
        front, back = set([beginWord]), set([endWord])
        wordDict.discard(beginWord)
        while front:
            # generate all valid transformations
            front = wordDict & (set(word[:index] + ch + word[index+1:] for word in front 
                                for index in range(len(beginWord)) for ch in 'abcdefghijklmnopqrstuvwxyz'))
            if front & back:
                # there are common elements in front and back, done
                return length
            length += 1
            
            if len(front) > len(back):
                # swap front and back for better performance (fewer choices in generating nextSet)
                front, back = back, front
            # remove transformations from wordDict to avoid cycle
            wordDict -= front
        return 0
         '''