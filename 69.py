from typing import List

# LeetCode / 240. Search a 2D Matrix II

class Solution:
    def binary_search(self, left: int, right: int, down: int, up: int, matrix: List[List[int]], target: int) -> bool:
        if left > right or down > up:
            return False


        mid_row = (left + right) // 2
        mid_col = (up + down) // 2

        if matrix[mid_col][mid_row] == target:
            return True
        elif matrix[mid_col][mid_row] < target:
            if self.binary_search(mid_row + 1, right, down, up, matrix, target):
                return True
            if self.binary_search(left, right, mid_col + 1, up, matrix, target):
                return True
        elif matrix[mid_col][mid_row] > target:
            if self.binary_search(left, mid_row - 1, down, up, matrix, target):
                return True
            if self.binary_search(left, right, down, mid_col - 1, matrix, target):
                return True
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.binary_search(0, len(matrix[0]) - 1, 0, len(matrix) - 1, matrix, target)


matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5

print(Solution().searchMatrix(matrix, target))