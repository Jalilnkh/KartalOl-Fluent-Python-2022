from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def construct_maximum_binary_tree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
    
        # Find the index of the maximum value
        max_index = nums.index(max(nums))
        
        # Create the root node with the maximum value
        root = TreeNode(nums[max_index])
        
        # Recursively build the left and right subtrees
        root.left = self.construct_maximum_binary_tree(nums[:max_index])
        root.right = self.construct_maximum_binary_tree(nums[max_index + 1:])
        
        return root
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.construct_maximum_binary_tree([1,2,2,4,5]))
    

