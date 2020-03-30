# AI20S - HW0
# Student ID                : R08922a02
# English Name              : Shuo-En
# Chinese Name (optional)   : 張碩恩


class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sum_of_left_leaves(self, _root):
        """
        :type _root: Node
        :return type: int
        """
        # your code
        # raise NotImplementedError
        sol = Solution()
        if _root == None:
            return 0
        elif _root.left != None and _root.left.left == None and _root.left.right == None:
            return _root.left.val + sol.sum_of_left_leaves(_root.right)
        else:
            return sol.sum_of_left_leaves(_root.left) + sol.sum_of_left_leaves(_root.right)


if __name__ == '__main__':
    # build tree
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)
    sol = Solution()
    print(sol.sum_of_left_leaves(root))


