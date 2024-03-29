'''

Leetcode 75-Binary search BFS 199 Binary Tree Right Side View
 
Given the root of a binary tree, imagine yourself standing on the right side of it, and return the values of the nodes you can see ordered from top to bottom.
 

Example 1:
    Input: root = [1,2,3,null,5,null,4]
    Output: [1,3,4]
    
Example 2:    
    Input: root = [1,null,3]
    Output: [1,3]
    
Example 3:    
    Input: root = []
    Output: []
 
Constraints:    
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    ans = []

    def dfs(root: Optional[TreeNode], depth: int) -> None:
      if not root:
        return

      if depth == len(ans):
        ans.append(root.val)
      dfs(root.right, depth + 1)
      dfs(root.left, depth + 1)

    dfs(root, 0)
    return ans


# Second solution

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def traverse(root, level):
            if not root: return 
            nonlocal res
            if len(res) < level + 1:
                res.append(root.val)
            traverse(root.right, level+1)
            traverse(root.left, level+1)
        
        traverse(root, 0)
        return res
