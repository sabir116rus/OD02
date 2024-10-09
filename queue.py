class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        # Проверка, пуста ли очередь
        return self.items == []

    def enqueue(self, item):
        # Добавление элемента в очередь
        self.items.insert(0, item)

    def dequeue(self):
        # Удаление и возвращение первого элемента
        return self.items.pop()

    def size(self):
        # Возвращение размера очереди
        return len(self.items)

# Пример использования:
queue = Queue()
queue.enqueue("Первый")
queue.enqueue("Второй")
queue.enqueue("Третий")
print(queue.dequeue())  # Ожидается "Первый"
print(queue.size())     # Ожидается 2
print(queue.is_empty()) # Ожидается False
