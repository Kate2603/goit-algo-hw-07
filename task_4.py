class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        self.replies.append(reply)

    def remove_reply(self):
        # Оновлюємо текст коментаря та прапорець is_deleted
        self.text = "Цей коментар було видалено."
        self.is_deleted = True
        # Відповіді не видаляються, щоб зберегти їх у дереві

    def display(self, indent=0):
        # Виводимо текст коментаря з відступом
        prefix = "    " * indent
        if self.is_deleted:
            print(f"{prefix}Цей коментар було видалено.")
        else:
            print(f"{prefix}{self.author}: {self.text}")
        # Рекурсивно виводимо відповіді
        for reply in self.replies:
            reply.display(indent + 1)

# Приклад використання
if __name__ == "__main__":
    root_comment = Comment("Яка чудова книга!", "Бодя")
    reply1 = Comment("Книга повне розчарування :(", "Андрій")
    reply2 = Comment("Що в ній чудового?", "Марина")

    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)

    reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
    reply1.add_reply(reply1_1)

    # Видаляємо відповідь
    reply1.remove_reply()

    # Виводимо коментарі
    root_comment.display()

