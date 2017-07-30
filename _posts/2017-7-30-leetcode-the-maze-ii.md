## Leetcode The Maze II

Here we used bfs (with heap) to implement Dijkstra

```
def shortestDistance(maze, start, destination):
    dest = tuple(destination)
    m, n = len(maze), len(maze[0])
    res = None
    def go(start, direction): # return stop position and length
        i, j = start
        ii, jj = direction
        l = 0
        while 0 <= i + ii < m and 0 <= j + jj < n and maze[i+ii][j+jj] != 1:
            i += ii
            j += jj
            l += 1
        return l, (i, j)
    # bfs (dijkstra)
    visited = {}
    q = []
    heapq.heappush(q, (0, tuple(start))) # use heap so we can always pick node with smallest distance
    while q:
        length, cur = heapq.heappop(q)
        if cur in visited and visited[cur] <= length: # no need to update since length is bigger
            continue
        visited[cur] = length
        if cur == dest:
            return length # first time found dest is the shortest
        for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            l, np = go(cur, direction)
            heapq.heappush(q, (length + l, np))
    return -1
```
