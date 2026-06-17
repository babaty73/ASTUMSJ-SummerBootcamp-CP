class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        result = []
        
        for row in image:
            reversed_row = row[::-1]
            inverted = [1 - x for x in reversed_row]
            result.append(inverted)
        return result
