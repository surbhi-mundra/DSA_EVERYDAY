""" 1252. Cells with Odd Values in a Matrix

There is an m x n matrix that is initialized to all 0's. There is also a 2D array indices where each indices[i] = [ri, ci] represents a 0-indexed location to perform some increment operations on the matrix.

For each location indices[i], do both of the following:

Increment all the cells on row ri.
Increment all the cells on column ci.
Given m, n, and indices, return the number of odd-valued cells in the matrix after applying the increment to all locations in indices.

 

Example 1:


Input: m = 2, n = 3, indices = [[0,1],[1,1]]
Output: 6
Explanation: Initial matrix = [[0,0,0],[0,0,0]].
After applying first increment it becomes [[1,2,1],[0,1,0]].
The final matrix is [[1,3,1],[1,3,1]], which contains 6 odd numbers.
Example 2:


Input: m = 2, n = 2, indices = [[1,1],[0,0]]
Output: 0
Explanation: Final matrix = [[2,2],[2,2]]. There are no odd numbers in the final matrix.
 

Constraints:

1 <= m, n <= 50
1 <= indices.length <= 100
0 <= ri < m
0 <= ci < n
 

Follow up: Could you solve this in O(n + m + indices.length) time with only O(n + m) extra space? """

#approach 1, Integer Counting Arrays
# Time Complexity: O(L + m + n) where L is len(indices)
# Space Complexity: O(m + n) for row and column counter arrays

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row_counts = [0] * m
        column_counts = [0] * n

        for r, c in indices:
            row_counts[r] += 1
            column_counts[c] += 1

        odd_rows = sum(count % 2 for count in row_counts)
        odd_columns = sum(count % 2 for count in column_counts)

        even_rows = m - odd_rows
        even_columns = n - odd_columns

        return (odd_rows * even_columns) + (even_rows * odd_columns)

#approach 2, Boolean Parity Flipping
# Time Complexity: O(L + m + n) where L is len(indices)
# Space Complexity: O(m + n) for row and column boolean arrays

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [False] * m
        columns = [False] * n

        for r, c in indices:
            rows[r] = not rows[r]
            columns[c] = not columns[c]

        odd_rows = sum(rows)
        odd_columns = sum(columns)

        return (odd_rows * (n - odd_columns)) + ((m - odd_rows) * odd_columns)
        
