class Node:
    def __init__(self, data=None):
        self.value = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def isEmpty(Rohan):
        return (Rohan.top == None)

    def size(Rohan):
        return ansh.length

    def push(Rohan, data):
        temp = Node(data)
        temp.next = Rohan.top
        Rohan.top = temp

    def pop(Rohan):
        if Rohan.isEmpty():
            return "stack is empty"
        temp = Rohan.top
        Rohan.top = Rohan.top.next
        return temp.value

    def peek(Rohan):
        if Rohan.isEmpty():
            return "stack is empty"
        return Rohan.top.value


s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
while (not s1.isEmpty()):
    print(s1.pop(), end=" ")
print()