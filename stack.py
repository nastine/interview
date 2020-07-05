# Необходимо реализовать класс Stack со следующими методами:
# isEmpty - проверка стека на пустоту. Метод возвращает True или False.
# push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
# pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
# peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
# size - возвращает количество элементов в стеке.

class Stack:
    def __init__(self, stack):
        self.stack = list(stack)
    
    def isEmpty(self):
        return (not self.stack)
    
    def push(self, element):
        self.stack.append(element)

    def pop(self):
        self.stack.pop()
        if len(self.stack) != 0:
            return self.stack[-1]

    def peek(self):
        return self.stack[-1]

    def m(self):
        return self.stack[:-1]

    def size(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)

if __name__ == "__main__":
    obj = Stack('(((([{}]))))')
    print(obj.isEmpty())
    obj.push('1')
    print(obj)
    print(obj.pop())
    print(obj.peek())
    print(obj.size())
    print(obj.m())
