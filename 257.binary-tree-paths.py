# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = set([])
        self.dfs(root, [], res)
        return list(res)
    def dfs(self, node, path, res):
        if not node: return
        if not node.left and not node.right:
            res.add('->'.join(path + [str(node.val)]))
            return
        self.dfs(node.left, path + [str(node.val)], res)
        self.dfs(node.right, path + [str(node.val)], res)