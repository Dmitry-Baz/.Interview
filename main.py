class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)
    
# Теперь мы можем использовать этот класс для проверки сбалансированности скобок:
    

def is_balanced(expression):
    stack = Stack()
    opening = "([{"
    closing = ")]}"
    matches = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty() or stack.pop() != matches[char]:
                return "Несбалансированно"

    return "Сбалансированно" if stack.is_empty() else "Несбалансированно"

# Пример использования
input_expression = input("Введите строку со скобками: ")
print(is_balanced(input_expression))