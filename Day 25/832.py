class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        return [list(map(lambda x: 1 - x, reversed(row))) for row in image]
