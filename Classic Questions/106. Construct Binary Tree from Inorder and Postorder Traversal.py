# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        node = TreeNode(postorder[-1])
        index = 0
        while index < len(inorder):
            if inorder[index] == postorder[-1]: 
                break
            index += 1
        
        print(postorder[-1])
        node.left = self.buildTree(inorder[:index], postorder[:index])
        node.right = self.buildTree(inorder[index+1:], postorder[index:-1])
        
        return node

