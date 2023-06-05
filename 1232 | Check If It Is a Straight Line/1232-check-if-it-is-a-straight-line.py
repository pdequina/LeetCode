class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        (x0, y0), (x1, y1) = coordinates[0], coordinates[1]
        dx, dy = x1 - x0, y1 - y0
        return all((x - x0) * dy == (y - y0) * dx for x, y in coordinates)
