class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def checker(msg):
    s = Stack()
    balanced = True
    index = 0

    while index < len(msg) and balanced:
        symbol = msg[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index = index +1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def modify_checker(words):
    b = Stack()
    status = True
    cur = 0

    while cur < len(words) and status:
        word = words[cur]
        if word in "({[":
            b.push(word)
        else:
            if b.isEmpty():
                balanced = False
            else:
                b.pop()

def matches(open,close):
    opens = "({["
    closes = "]})"

print(checker('((()))'))
