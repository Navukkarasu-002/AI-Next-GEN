# Creation linked list
class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
    head = None
    tail = None

    newnode = Node(10)

    if head ==None and tail == None :
      head =newnode
      tail = newnode

    newnode = Node(20)
    tail.next = newnode
    tail = newnode

    temp = head
    while temp != None:
      print(temp.data)
      temp = temp.next
    print(None)



# stack
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    # 1. PUSH:
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    # 2. POP:
    def pop(self):
        if self.top is None:
            return "Stack is empty!"
        popped_value = self.top.data
        self.top = self.top.next
        return popped_value

    # 3. PEEK:
    def peek(self):
        if self.top is None:
            return "Stack is empty!"
        return self.top.data

    # 4. VIEW:
    def display(self):
        current = self.top
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


s = Stack()
s.push(10)
s.push(20)
s.push(30)

s.display()           # Output: 30 -> 20 -> 10 -> None
print("Top:", s.peek()) # Output: Top: 30
print("Popped:", s.pop()) # Output: Popped: 30
s.display()           # Output: 20 -> 10 -> None


# Queue
queue = []
front = -1
rear = -1
#enqueue
def enqueue(data):
    global front, rear
    queue.append(data)
    rear += 1
    if front == -1:
        front = 0
    print(data, "inserted")

#dequeue
def dequeue():
    global front, rear
    if front == -1 or front > rear:
        print("Queue is Empty")
    else:
        print("Deleted Element:", queue[front])
        front += 1

        if front > rear:
            front = rear = -1
enqueue(10)
enqueue(20)
enqueue(30)
print("Queue:", queue)
dequeue()
print("Queue after dequeue:", queue)
