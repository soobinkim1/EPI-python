from _data_structures import *

#min heap
#Arr[(i-1)/2] is parent node
#Arr[(2*i)+1] left child node
#Arr[(2*1)+2] right child node
#valid min-heap
valid = Binary_Tree(2)
valid.left = Binary_Tree(3)
valid.right = Binary_Tree(4)
valid.left.left = Binary_Tree(5)
valid.left.right = Binary_Tree(6)
valid.right.left = Binary_Tree(8)
valid.right.right = Binary_Tree(10)
#[2,3,4,5,6,8,10]
#invalid min-heap
invalid = Binary_Tree(5)
invalid.left = Binary_Tree(3)
invalid.right = Binary_Tree(8)
invalid.left.left = Binary_Tree(2)
invalid.left.right = Binary_Tree(4)
invalid.right.left = Binary_Tree(6)
invalid.right.right = Binary_Tree(10)
#[5,3,8,2,4,6,10]