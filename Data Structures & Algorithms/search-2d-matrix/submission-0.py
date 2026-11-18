class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        startRow, endRow = 0, len(matrix) - 1
        while startRow <= endRow:
            midRow = (startRow + endRow) // 2
            if matrix[midRow][0] <= target and matrix[midRow][len(matrix[midRow]) - 1] >= target:
                start, end = 0, len(matrix[midRow]) - 1
                while start <= end:
                    mid = (start + end) // 2
                    if matrix[midRow][mid] == target:
                        return True
                    elif matrix[midRow][mid] < target:
                        start = mid + 1
                    else:
                        end = mid - 1
                return False
            elif matrix[midRow][0] < target:
                startRow = midRow + 1
            else:
                endRow = midRow - 1
            
        return False