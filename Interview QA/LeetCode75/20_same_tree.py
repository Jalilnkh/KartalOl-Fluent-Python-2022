# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_same_tree(self, p, q) -> bool:
        # If both trees are empty
        if not p and not q:
            return True
        # If one of the trees is empty
        if not p or not q:
            return False
        # If the current nodes' values are different
        if p.val != q.val:
            return False
        # Recursively check left and right subtrees
        return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)
    

if __name__ == "__main__":
    sol = Solution()
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    # Tree 2
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    q.right = TreeNode(4)
    
    print(sol.is_same_tree(p,q))
