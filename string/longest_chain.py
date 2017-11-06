import sys

def FindLongestChain(words):
    if words is None or len(words)==0:
        return None
    longest_chain = 0
    map = dict()
    words.sort(key = lambda s: len(s))    
    for word in words:
        if word not in map:
            map[word] = 1
        for i in range(0, len(word)):
            subword = word[:i] + word[i+1:]
            if subword in map and map[subword] + 1 > map[word]:
                map[word] = map[subword] + 1
        if map[word] > longest_chain:
            longest_chain = map[word]
    return longest_chain


print(FindLongestChain(["a", "b", "ba", "bca", "bda", "bdca"]))
