class Solution(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        n = len(bombs)
        graph = [[] for _ in range(n)]
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2, r2 = bombs[j]
                if (x1 - x2)**2 + (y1 - y2)**2 <= r1**2:
                    graph[i].append(j)
            result = 0
            for i in range(n):
                visited = [False] * n
                visited[i] = True
                queue = deque([i])
                detonations = 1
                while queue:
                    check = queue.popleft()
                    for neighbor in graph[check]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                            detonations += 1
                result = max(result, detonations)
        return result
