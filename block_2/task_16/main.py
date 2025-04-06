class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,key):
        def _insert(node, key):
            if not node:
                return Node(key)
            if key < node.key:
                node.left = _insert(node.left, key)
                node.left.parent = node
            else:
                node.right = _insert(node.right, key)
                node.right.parent = node
            return node

        self.root = _insert(self.root, key)

    def max(self, poss):
        result = None
        count = 0

        def _reverse_inorder(node):
            nonlocal count, result
            if not node or result is not None:
                return

            _reverse_inorder(node.right)

            count += 1
            if count == poss:
                result = node.key
                return

            _reverse_inorder(node.left)

        _reverse_inorder(self.root)
        return result

    def check(self, check_key):
        def _check(node, check_key):
            if not node:
                return None

            if check_key == node.key:
                return node.key, node.left, node.right, node.parent
            if check_key < node.key:
                return _check(node.left, check_key)
            else:
                return _check(node.right, check_key)

        return _check(self.root, check_key)

    def delete(self,delete_key):
        def _delete(node, delete_key):
            if not Node:
                return None

            if delete_key < node.key:
                node.left = _delete(node.left, delete_key)
            elif delete_key > node.key:
                node.right = _delete(node.right, delete_key)
            else:
                if not node.left and not node.right:
                    return None
                elif not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    successor = node.right
                    while successor.left:
                        successor = successor.left
                    node.key = successor.key
                    node.right = _delete(node.right, successor.key)
            return node

        self.root = _delete(self.root, delete_key)

bst_obj = BST()


i_file = open("input.txt", 'r')
n = int(i_file.readline())
o_file = open("output.txt", 'w')

for i in range(n):
    request = list(i_file.readline().split())
    command = request[0]
    key = int(request[1])
    if command == "+1" or command == "1":
        bst_obj.insert(key)
    elif command == "0":
        o_file.write(str(bst_obj.max(key)) + '\n')
    elif command == "-1":
        bst_obj.delete(key)
    elif command == "?":
        print(bst_obj.check(key))
    else:
        print("Incorrect command in %s string" % i)
o_file.close()
i_file.close()
