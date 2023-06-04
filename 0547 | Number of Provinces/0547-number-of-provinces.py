class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        visited = set()
        result = 0
        def dfs(start):
            for k in range(len(isConnected[start])):
                if isConnected[start][k] == 1 and k not in visited:
                    visited.add(k)
                    dfs(k)
        for row in range(len(isConnected[0])):
            if isConnected[row][row] == 1 and row not in visited:
                visited.add(row)
                dfs(row)
                result += 1
        return result
