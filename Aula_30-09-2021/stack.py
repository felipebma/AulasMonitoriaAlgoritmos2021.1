class Node:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None
    
class Stack:

    def __init__(self) -> None:
        self.top = None
        self.size = 0
    
    # O(1)
    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
    
    # O(1)
    def pop(self):
        if self.top == None:
            return None
        self.size -= 1
        value = self.top.value
        self.top = self.top.next
        return value
    
    # O(1)
    def peek(self):
        if self.top == None:
            return None
        value = self.top.value
        return value

    # O(1)
    def is_empty(self):
        return self.size == 0

    # O(n)
    def search(self, value):
        aux = self.top
        while aux != None:
            if aux.value == value:
                return True
            aux = aux.next
        return False

    # O(n^2)
    def __str__(self) -> str:
        result = []
        aux = self.top
        while aux != None:
            result.append(str(aux.value) + " ")
            aux = aux.next
        return result.strip()
        
# str ="4" -> 1
# str ="4 3" -> 2
# str ="4 3 2" -> 3 
# str ="4 3 2 1" -> 4
# str ="5 4 3 2 1" -> 5

# x*(x+1)/2 = O ((x^2 + x)/2) -> O(x²/2) -> O(x²)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack)
print(stack.search(4))
stack.pop()
print(stack)
print(stack.search(4))
