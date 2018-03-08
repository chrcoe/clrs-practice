'''
This is the binary search tree implementation.
'''

class BinSearchTree():

    class Node():

        def __init__(self, key, parent, data, left_child, right_child):
            self.key = key
            self.parent = parent
            self.data = data
            self.left = left_child
            self.right = right_child

        def __str__(self):
            return 'Key: {}, Parent: {}, Data: {}, Left: {}, Right: {}'.format(
                self.key, self.parent, self.data, self.left, self.right
            )

    def min(self):
        pass

    def max(self):
        pass

    def inorder_tree_traversal(self, root):
        ''' 
        Recursive implementation for inorder tree traversal.
        This just prints out the key and moves on.
        '''
        inorder_tree_traversal(root.left)
        print(root.key)
        inorder_tree_traversal(root.right)
