# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution using recursion
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 == None or t2 == None:
            return t1 or t2 # will return the non-None value,or if both None, None.
        # t1.left is merged result of t1.left and t2.left
        # t1.right is merged result of t1.right and t2.right

        t1.val = t1.val + t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

# Initial attempt. Slow & uses lots of memories due to queues. Insight is that you can just use recursion, since this is a repeating tree structure
class xSolution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 == None or t2 == None:
            return t1 or t2 # return value that's not None, or None if both are None
        # breadth-first search to traverse both trees
        # if corresponding node in t2, add to t1 value
        # by adding, creates a new corresponding node in t3 which will allow for continued traaversal in line with t2's structure
        head = t1
        queue1 = [t1]
        queue2 = [t2]
        
        while (len(queue1) > 0):
            temp1 = queue1.pop(0)
            temp2 = queue2.pop(0)
            
            temp1.val = temp1.val + temp2.val
            
            # if only one of the two exist, create new node
            if (temp1.left != None) ^ (temp2.left != None):
                temp1.left = TreeNode(0) if temp1.left == None else temp1.left
                temp2.left = TreeNode(0) if temp2.left == None else temp2.left
            
            if (temp1.right != None) ^ (temp2.right != None):
                temp1.right = TreeNode(0) if temp1.right == None else temp1.right
                temp2.right = TreeNode(0) if temp2.right == None else temp2.right
            
             
            if temp1.left != None:
                queue1.append(temp1.left)
            if temp2.left != None:
                queue2.append(temp2.left)
            
            if temp1.right != None:
                queue1.append(temp1.right)
            if temp2.right != None:
                queue2.append(temp2.right)
                
        return head

class Solution2:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode: 