import collections
import copy

linked_list=collections.namedtuple("myList",['element', 'next'])

#create list with all the elements

for i in range(50):
    if i==0:
        node=linked_list(i,None)
    else:
        node=linked_list(i,node)

head=node

# while head is not None:
#     print(head.element)
#     head=head.next
print(node)
counter=0
while head is not None:
    head=head.next
    counter +=1
    if counter==20:
        print(head.element)
        break

# Another method
head=node
counter=0
while head is not None:
    head = head.next
    counter +=1
    if counter == 20:
        head2=copy.copy(head)
        break
print(head2.element)


# Print all the nodes of level order tree

node = collections.namedtuple('treenode',['left','element','right'])

# create a tree of depth 3
i=0
n2_l=node(None,2*i+5,None)
n2=node(n2_l,2*i+2,None)

n1_l=node(None,2*i+3,None)
n1_r=node(None,2*i+4,None)
n1 = node(n1_l,2*i+1,n1_r)

root_node=node(n1,i,n2)
# height of the node

def height(node):
    if node.left is None and node.right is None:
        return 0
    else:
        if node.left is not None:
            lheight = 1 + height(node.left)
        if node.right is not None:
            rheight = 1 + height(node.right)
        try:
            return max(lheight,rheight)
        except NameError:
            return lheight
        except NameError:
            return rheight

print(height(root_node))

def pre_order(node):
    print(node.element, end=" ")
    if height(node) > 0:
        try:
            pre_order(node.left)
        except:
            pass
        try:
            pre_order(node.right)
        except:
            pass

pre_order(root_node)
print("\n")
# print(root_node)

def post_order(node):
    if height(node) > 0:
        try:
            post_order(node.left)
        except:
            pass
        try:
            post_order(node.right)
        except:
            pass
    print(node.element, end=" ")

post_order(root_node)
print("\n")

def in_order(node):
    try:
        in_order(node.left)
    except:
        pass
    print(node.element, end=" ")
    try:
        in_order(node.right)
    except:
        pass

in_order(root_node)
print('\n')

def level_order(node,depth=0):
    if depth==0:
        print(node.element, end=" ")
        depth +=1
    else:
        try:
            print(node.left.element,node.right.element, end=" ")
        except:
            pass
        try:
            level_order(node.left,depth)
        except:
            pass
        try:
            level_order(node.right, depth)
        except:
            pass

level_order(root_node)


# Function to  print level order traversal of tree
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h + 1):
        printGivenLevel(root, i)

    # Print nodes at a given level


def printGivenLevel(root, level):
    if level == 0:
        print(root.element,end= " ")
    if level == 1:
        try:
            print(root.left.element,end=" ")
        except:
            pass
        try:
            print(root.right.element,end=" ")
        except:
            pass
    elif level > 1:
        printGivenLevel(root.left, level - 1)
        printGivenLevel(root.right, level - 1)

printLevelOrder(root_node)