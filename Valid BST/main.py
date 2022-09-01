# Ted Lawson
from idlelib.tree import TreeNode


class Solution:
    def valid_BST(self, root: TreeNode) -> bool:

        def test_node(node, left, right):
            if not node:
                return True

            if not (left < node.val < right):
                return False

            return (test_node(node.left, left, node.val) and
                    test_node(node.right, node.val, right))

        return test_node(root, float('-inf'), float('inf'))


def main():
    root = [5, 1, 4, None, None, 3, 6]
    answer = Solution().valid_BST(root)
    print(answer)


if __name__ == '__main__':
    main()
