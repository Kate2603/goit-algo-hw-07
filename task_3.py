class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def sum_of_values(root):
    if root is None:
        return 0  # Базовий випадок: порожнє піддерево не додає нічого до суми

    # Рекурсивно знаходимо суму значень лівого і правого піддерев
    left_sum = sum_of_values(root.left)
    right_sum = sum_of_values(root.right)

    # Повертаємо суму значень вузла та обох піддерев
    return root.value + left_sum + right_sum

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

    total_sum = sum_of_values(root)
    print("Сума всіх значень у дереві:", total_sum)
