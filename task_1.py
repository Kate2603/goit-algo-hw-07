class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def find_max_value(root):
    current = root
    # йдемо до самого правого вузла
    while current.right is not None:
        current = current.right
    return current.value

# Приклад використання
if __name__ == "__main__":
    # Створення дерева
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(25)

    max_value = find_max_value(root)
    print("Найбільше значення у дереві:", max_value)
