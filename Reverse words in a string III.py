#leetcode problem 557 reverse words in a string
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()

        for i in range(len(words)):
            words[i] = words[i][::-1]

        return " ".join(words)
