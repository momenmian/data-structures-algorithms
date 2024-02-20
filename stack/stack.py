def stack():
    return 'stack' 


def queue():
    return 'queue'


def deque():
    return 'deque'


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return not self.items

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return not self.items

    def size(self):
        return len(self.items)
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]


def evaluate_expression(expression):
    stack = Stack()
    for char in expression:
        if char in '0123456789':
            stack.push(int(char))
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            if char == '+':
                stack.push(num1 + num2)
            elif char == '-':
                stack.push(num1 - num2)
            elif char == '*':
                stack.push(num1 * num2)
            elif char == '/':   
                assert num2 != 0, "Division by zero"
                stack.push(num1 / num2)
    return stack.pop()


# Test cases
print(evaluate_expression("123+4-5*6/7"))
print(evaluate_expression("1+2*3/4-5"))   # Output: 0
print(evaluate_expression("1+2*3/4-5*6")) # Output: -17s