class LLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, key, value):
        new_node = LLNode(key, value)
        new_node.next = self.head
        self.head = new_node

    def search(self, key):
        current = self.head
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        current = self.head
        previous = None
        while current is not None:
            if current.key == key:
                if previous is None: # If the node to delete is the head
                    self.head = current.next
                else:
                    previous.next = current.next # If the node to delete is not the head, update the previous node's next pointer
                return True
            previous = current
            current = current.next
        return False
    
    def traverse(self):
        current = self.head
        while current is not None:
            print(f"{current.key}: {current.value}")
            current = current.next
    
    