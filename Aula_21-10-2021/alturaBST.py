class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        self.altura = 1


def atualizaAltura(node):
    if node == None:
        return 0
    node.altura = max(node.altura, atualizaAltura(node.left) + 1)
    node.altura = max(node.altura, atualizaAltura(node.right) + 1)
    return node.altura


root = Node(1)
left = Node(2)
root.left = left
left_right = Node(3)
left.right = left_right
print(root.altura)
print(left.altura)
print(left_right.altura)
print("-------------")
atualizaAltura(root)
print(root.altura)
print(left.altura)
print(left_right.altura)
