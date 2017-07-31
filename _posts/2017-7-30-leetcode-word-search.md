Word search by using DFS.
I tried both with and without recursion. Without recursion I need to keep track of the path for current element, can't just use `visited` set because if an element is visited but not used for one path, it shouldn't be eliminated since other path may find it useful.
```
"""79. Word Search"""
# DFS without recursion
class Solution(object):
    def exist(self, board, word):
        # edge cases: word = ''
        m, n = len(board), len(board[0])
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == word[0]:
                    stack = [(i, j, 0, set([(i, j)]))]
                    while stack:
                        si, sj, k, path = stack.pop()
                        if k == len(word) - 1:
                            return True
                        for ni, nj in [(si+1, sj), (si-1, sj), (si, sj+1), (si, sj-1)]:
                            if ni >= 0 and ni < m and nj >= 0 and nj < n:
                                if (ni, nj) not in path and board[ni][nj] == word[k+1]:
                                    stack.append((ni, nj, k+1, path | set([(ni, nj)])))
        return False

# DFS with recursion
# implementation 1
def find_word(word, board):
    # edge cases: word = ''
    for i in xrange(len(board)):
        for j in xrange(len(board[0])):
            if search(board, i, j, word):
                return True
    return False
def search(board, i, j, word):
    if word == '':
        return True
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
        return False
    if board[i][j] == word[0]:
        board[i][j] = 0
        for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if search(board, ni, nj, word[1:]):
                return True
    return False
# implementation 2
class Solution(object):
    def _dfs(self, board, i, j, word):
        if len(word) == 0:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
            return False
        tmp = board[i][j]
        board[i][j] = '#'
        res = self._dfs(board, i+1, j, word[1:]) or self._dfs(board, i-1, j, word[1:]) \
        or self._dfs(board, i, j+1, word[1:]) or self._dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res
    def exist(self, board, word):
        if not board:
            return False
        # try every element in the matrix as starting point until found word
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self._dfs(board, i, j, word):
                    return True
        return False


"""
212. Word Search II

o a a n
e t a e
i h k r
i f l v

eat, oath
"""
# DFS without recursion
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        res = set()
        m, n = len(board), len(board[0])
        for i in xrange(m):
            for j in xrange(n):
                for word in words:
                    if board[i][j] == word[0]:
                        stack = [(i, j, 0, set([(i, j)]))]
                        while stack: # everything in stack in board, match word and first time visit
                            si, sj, k, path = stack.pop()
                            if k == len(word) - 1:
                                res.add(word)
                                break
                            for ni, nj in [(si+1, sj), (si-1, sj), (si, sj+1), (si, sj-1)]:
                                if ni >= 0 and ni < m and nj >= 0 and nj < n:
                                    if (ni, nj) not in path and board[ni][nj] == word[k+1]:
                                        stack.append((ni, nj, k+1, path | set([(ni, nj)])))
        return list(res)

board = [['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e'], ['i', 'h', 'k', 'r'], ['i', 'f', 'l', 'v']]
words = ["oath","pea","eat","rain"]

board = [
    ['a', 'b'],
    ['a', 'a']
]
words = ["aba","baa","bab","aaab","aaa","aaaa","aaba"]

solution = Solution()
print solution.findWords(board, words)
```
