class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def find_min_value_recursive(root):
    if root is None:
        return None  # Дерево порожнє, найменше значення не існує
    
    if root.left is None:
        return root.value  # Досягли найменшого вузла

    return find_min_value_recursive(root.left)  # Рекурсивний виклик для лівого піддерева

# Приклад використання
if __name__ == "__main__":
    # Створення дерева
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(20)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(25)

    min_value = find_min_value_recursive(root)
    print("Найменше значення у дереві:", min_value)
