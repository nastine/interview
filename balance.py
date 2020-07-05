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
