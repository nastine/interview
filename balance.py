# Используя стек из задания 1 необходимо решить задачу на проверку сбалансированности скобок. Сбалансированность скобок означает, что каждый открывающий символ имеет соответствующий ему закрывающий, и пары скобок правильно вложены друг в друга. Сбалансированными последовательности будут следующие скобки:

# Программа ожидает на вход строку со скобками. На выход сообщение "Сбалансированно", если строка корректная и "Небалансированно", если строка составлена не верно.
from stack import Stack




def is_balanced(string):
    brackets_open = ('(', '[', '{', '<')
    brackets_closed = (')', ']', '}', '>')
    stack = Stack('')
    for i in string:
        if i in brackets_open:
            stack.push(i)
        if i in brackets_closed:    
            if stack.size() == 0:
                return print('Несбалансировано')
            index = brackets_closed.index(i)
            open_bracket = brackets_open[index]
            if stack.peek() == open_bracket:
                stack.pop()
            else: 
                return print('Несбалансировано')
    return print('Сбалансировано')

is_balanced('(((([{}]))))')
is_balanced('[([])((([[[]]])))]{()}')
is_balanced('{{[()]}}') 
# Несбалансированными последовательности:
is_balanced(')}{}')
is_balanced('{{[(])]}}')
is_balanced('[[{())}]')