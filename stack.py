class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        # Проверка, пуст ли стек
        return self.items == []

    def push(self, item):
        # Добавление элемента в стек
        self.items.append(item)

    def pop(self):
        # Удаление и возвращение верхнего элемента
        return self.items.pop()

    def peek(self):
        # Просмотр верхнего элемента без его удаления
        return self.items[-1]

    def size(self):
        # Возвращение размера стека
        return len(self.items)

# Пример использования:
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.peek())   # Ожидается 30
print(stack.pop())    # Ожидается 30
print(stack.is_empty())  # Ожидается False
print(stack.size())   # Ожидается 2
