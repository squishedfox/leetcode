# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self._counts = dict[int, int]()

    def findMode(self, root: TreeNode) -> list[int]:
        if root is None:
            return []

        self.updateModeCounts(root)
        keys = []
        for key, value in self._counts.items():
            if len(keys) == 0:
                keys.append(key)
                continue
            for k in keys:
                if self._counts[k] == value and k != key:
                    keys.append(key)
                    break
                if value > self._counts[k]:
                    keys = [key] # should be greater than all the others

        return keys

    def updateModeCounts(self, root: TreeNode) -> None:
        if root is None:
            return
        if root.val not in self._counts.keys():
            self._counts.update({root.val: 0})
        
        self._counts[root.val] += 1

        self.updateModeCounts(root.left)
        self.updateModeCounts(root.right)


root = TreeNode(
    val=1,
    left=None,
    right=TreeNode(
        val=2,
        left=None,
        right=None
    )
)

print(Solution().findMode(root))
