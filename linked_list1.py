class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node("1st Node")
head.next = Node("2nd Node")
head.next.next =  Node("3rd Node")

print(head.value) # Outputs "1st Node"
print(head.next.value) # Outputs "2nd Node"
print(head.next.next.value) # Outputs "3rd Node"