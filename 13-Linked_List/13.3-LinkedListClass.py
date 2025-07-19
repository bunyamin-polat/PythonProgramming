class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None 
    
    # Insert
    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return self.head
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
    
    def insert_at_index(self, index, data):
        if index < 0:
            return None
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return self.head
        
        temp = self.head
        current_index = 0
        while temp is not None and current_index < index - 1:
            temp = temp.next
            current_index += 1
            
        if temp is None:
            return None
        
        new_node.next = temp.next
        temp.next = new_node
        
        return self.head
    
    # Delete
    def delete_at_head(self):
        if self.head is None:
            return None
        self.head = self.head.next
        return self.head

    def delete_at_index(self, index):
        if index < 0 or self.head is None:
            return None
        if index == 0:
            self.head = self.head.next
            return self.head
        
        temp = self.head
        current_index = 0
        
        while temp is not None and current_index < index - 1:
            temp = temp.next
            current_index += 1
            
        if temp is None or temp.next is None:
            return None
        
        temp.next = temp.next.next
        
        return self.head
    
    def delete_at_tail(self):
        if self.head is None:
            return None
        if self.head.next is None:
            self.head = None
            return self.head
        
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None
        
        return self.head
    
    def delete_node_by_value(self, value):
        if self.head is None:
            return None
        if self.head.data == value:
            self.head = self.head.next
            return self.head
        
        temp = self.head
        while temp.next is not None and temp.next.data != value:
            temp = temp.next
        
        if temp.next is not None:
            temp.next = temp.next.next
        return self.head
    
    # Search
    
    def search_by_value(self, value):
        temp = self.head
        index = 0
        while temp is not None:
            if temp.data == value:
                return temp, index
            temp = temp.next
            index += 1
        return None, -1
    
    def search_by_index(self, index):
        temp = self.head
        current_index = 0
        while temp is not None:
            if current_index == index:
                return temp.data
            temp = temp.next
            current_index += 1
        return None
    
    # Update
    def update_node(self, index, new_value):
        temp = self.head
        current_index = 0
        while temp is not None:
            if current_index == index:
                temp.data = new_value
                return self.head
            temp = temp.next
            current_index += 1
        return None
    
    # Print
    def print_LL(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
    
    # Length
    def length_LL(self):
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next
        return count
    
    # Create linked list from a list of values
    def create_ll_from_list(self, data_list):
        self.head = None
        tail = None
        for data in data_list:
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node
        return self.head
