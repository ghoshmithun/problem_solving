class Node:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None

    def insert(self,val):
        if self.data==val:
            return False
        elif self.data > val:
            if self.leftChild:
                self.leftChild.insert(val)
            else:
                self.leftChild=Node(val)
        else:
            if self.rightChild:
                self.rightChild.insert(val)
            else:
                self.rightChild=Node(val)

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.data))
            if self.rightChild:
                self.rightChild.inorder()



# class Tree:
#     def __init__(self):
#         self.root=None
#
#     def insert(self,val):
#         if self.root==None:
#             self.root=Node(val)
#         elif self.root.data > val:
#             if self.root.leftChild==None:
#                 self.root.leftChild=Node(val)
#             else:
#                 self.root.leftChild.insert(val)
#         else:
#             if self.root.rightChild == None:
#                 self.root.rightChild = Node(val)
#             else:
#                 self.root.rightChild.insert(val)
#
#     def __str__(self):
#         'inorder traversal'
#         if self:
#             return self.root.inorder()


def height_tree(tree):
    if not tree:
        return 0
    else:
        ltree=tree.leftChild
        rtree=tree.rightChild
        lDepth=height_tree(ltree)
        rDepth=height_tree(rtree)
        if abs(lDepth - rDepth ) > 1:
            return False
    return True


if __name__ == '__main__':
    tree = Node(5)
    tree.insert(10)
    tree.insert(12)
    tree.insert(5)
    tree.insert(4)
    tree.insert(20)
    tree.insert(8)
    tree.insert(7)
    tree.insert(15)
    tree.insert(13)
    tree.inorder()
    print(height_tree(tree))
