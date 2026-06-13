#leetcode problem 867
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = list(zip(*matrix))
        return result
