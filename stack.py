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
