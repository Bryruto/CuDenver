# A binary search tree that stores unique, mutually comparable values.
# At every node, all values in the left subtree are smaller and all values
# in the right subtree are larger. This tree does not balance itself.


class Node:
    # Store one value and references to its left and right children.

    def __init__(self,value):
        # Create a node with no children; None means a child is absent.
        self.value = value 
        self.left: Node | None = None
        self.right: Node | None = None

class BST:
    # Manage the root node and the number of unique values in the tree.

    def __init__(self):
        # Start with an empty tree.
        self.root: Node | None = None # The root is the starting node.
        self.count = 0

    def insert(self,value):
        # Insert one value, ignoring duplicates, and return None.
        # Follow one path to an empty child position. This takes O(h) time
        # and O(1) extra space, where h is the tree height. In a tree with
        # n nodes, h can be as large as n because the tree is not balanced.
        # The first inserted value becomes the root.
        if self.root is None:
            self.root = Node(value)
            self.count += 1
            return
            
        # Move through existing nodes until an empty child is found.
        curr = self.root
        while True:
            if value < curr.value:
                # Smaller values belong in the left subtree.
                if curr.left is None:
                    curr.left  = Node(value)
                    break
                curr = curr.left

            elif value > curr.value:
                # Larger values belong in the right subtree.
                if curr.right is None:
                    curr.right = Node(value)
                    break
                curr = curr.right 
            else:
                # An equal value already exists; leave the count unchanged.
                return

        # A new child was attached before the loop ended with break.
        self.count+=1


    def search(self,value) -> bool:
        # follow comparisons to find one value
        # return true when found or false when absent
        # search time depends on tree height and uses constant extra space
        curr = self.root

        while curr is not None:
            if value == curr.value:
                return True
            elif value < curr.value:
                # only the left subtree can contain a smaller value
                curr = curr.left
            else:
                # only the right subtree can contain a larger value
                curr = curr.right

        # reaching an empty child means the value is not in the tree
        return False


def test_search_empty_tree():
    # an empty tree contains no keys
    tree = BST()
    assert tree.search(5) is False


def test_search_present_and_absent_keys():
    # check the root and both subtrees against expected membership
    values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    tree = BST()
    for value in values:
        tree.insert(value)
    for key in range(-1, 17):
        assert tree.search(key) is (key in values)


def test_duplicate_insertion():
    # duplicates remain searchable without increasing the unique count
    tree = BST()
    for value in [5, 3, 7, 5, 3, 7]:
        tree.insert(value)
    assert tree.count == 3
    for key in [3, 5, 7]:
        assert tree.search(key) is True
    assert tree.search(6) is False

