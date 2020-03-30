class BstNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right

def rebuild_bst_from_preorder(preorder_sequence: List[int]
                              ) -> Optional[BstNode]:
    if len(preorder_sequence) == 0:
        return None
    # maintain a stack of nodes that are candidates for more left node or right nod
    # loop through n in list
    # if n is smaller than the last node in stack, lastNode.left = newNode, stack.append(newNode)
    # if n is greater than lastNode, for i range(len(stack)-1, 0, -1), pop each node unless stack[i-1] > n > stack[i], then stack[-1].right = newNode
        # if n is greater than all Nodes in stack, only the first node will be left, in which case firstNode.right = newNode
    # after adding right node to any lastNode, pop lastNode from the stack
    firstNode = BstNode(preorder_sequence[0])
    stack = [firstNode]
    for n in preorder_sequence[1:]:
        newNode = BstNode(n)
        if newNode.data < stack[-1].data:
            stack[-1].left = newNode
            stack.append(newNode)
        else:
            for i in range(len(stack)-1, 0, -1):
                if stack[i-1].data > n > stack[i].data:
                    break
                else:
                    stack.pop()
            stack[-1].right = newNode
            # since the last node has been assigned .right, it can be removed from stack
            stack.pop()
            stack.append(newNode)
    return firstNode
