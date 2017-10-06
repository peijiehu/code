class Solution(object):
    def leastBricks(self, wall):
        d = {}
        max_edges = 0
        for row in wall:
            cur = 0
            for brick in row[:-1]:
                cur += brick
                d[cur] = d.get(cur, 0) + 1
                max_edges = max(d[cur], max_edges)
        return len(wall) - max_edges

    def leastBricksTLE(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        width_set = set()
        for row in wall:
            cur = 0
            for i in range(0, len(row) - 1):
                cur += row[i]
                width_set.add(cur)
        ans = len(wall)
        for width in width_set:
            count = 0
            for row in wall:
                cur = 0
                i = 0
                while i < len(row) and cur < width:
                    cur += row[i]
                    i += 1
                if cur > width:
                    count += 1
            ans = min(ans, count)
        return ans
