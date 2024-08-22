# Maximum Depth Binary Tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def depth_tree(root):
    if root is None:
        return 0
    left_depth = depth_tree(root.left)
    right_depth = depth_tree(root.right)

    if left_depth > right_depth:
        return left_depth + 1
    else:
        return right_depth + 1


def depth_tree_v2(root):
    if root is None:
        return 0

    left_depth = depth_tree(root.left)
    right_depth = depth_tree(root.right)

    if left_depth > right_depth:
        return left_depth + 1
    else:
        return right_depth + 1


def validate_binary_search(root: TreeNode):
    if root is None: return True

    if root.left is not None:
        if root.left.val >= root.val:
            return False
        if not validate_binary_search(root.left):
            return False

    if root.right is not None:
        if root.right.val >= root.val:
            return False
        if not validate_binary_search(root.right):
            return False

    return True


# Symmetric Tree

def symmetric_tree(root):
    from collections import deque

    queue = deque([root, root])

    while queue:
        node1 = queue.popleft()
        node2 = queue.popleft()

        if not node1 and not node2:
            return False

        if not node1 or not node2 or node1.val != node2.val:
            return False

        queue.append(node1.left)
        queue.append(node2.right)
        queue.append(node1.right)
        queue.append(node2.left)

    return True

