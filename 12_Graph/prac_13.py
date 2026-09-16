from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):

        if endWord not in wordList:
            return 0

        wordSet = set(wordList)
        queue = deque()
        queue.append((beginWord, 1))

        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            for i in range(len(word)):
                original = word[i]
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch == original:
                        continue
                    newWord = word[:i] + ch + word[i+1:]
                    if newWord in wordSet:
                        wordSet.remove(newWord)
                        queue.append((newWord, steps + 1))

        return 0