class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_LL(head):
    temp = head # Assign head to temp to avoid changing head
    while temp is not None:
        print(temp.data, end = ' -> ')
        temp = temp.next
    print("None")

def take_input_better():
    value = int(input('Enter the value of the node: '))
    head = None
    tail = None
    
    while value != -1:
        new_node = Node(value)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
            
        value = int(input('Enter the value of the node: '))
        
    return head

def create_ll_from_list(values):
    head = None
    tail = None
    
    for value in values:
        new_node = Node(value)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node # Link the new node to the end of the list
            tail = new_node # Update tail to the new node
            
    return head