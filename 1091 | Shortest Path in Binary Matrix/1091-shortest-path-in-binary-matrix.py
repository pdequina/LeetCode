class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        queue = deque([(0,0,1)])
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        while queue:
            row, col, length = queue.popleft()
            if row == n-1 and col == n-1:
                return length
            for i, j in directions:
                nextRow = i + row
                nextCol = j + col
                if 0 <= nextRow < n and 0 <= nextCol < n and grid[nextRow][nextCol] == 0:
                    grid[nextRow][nextCol] = 1
                    queue.append((nextRow, nextCol, length + 1))
        return -1
