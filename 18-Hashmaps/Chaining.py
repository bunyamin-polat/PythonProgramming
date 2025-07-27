from LinkedListForChaining import LinkedList, LLNode

class HashmapUsingChaining:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.buckets = self.__create_buckets(self.capacity)

    def __create_buckets(self, capacity):
        return [LinkedList() for _ in range(capacity)]

    def __hash_function(self, key):
        return abs(hash(key)) % self.capacity

    def __rehash(self):
        print("Rehashing...")
        old_buckets = self.buckets # Store the old buckets
        self.capacity *= 2 # Double the capacity
        self.size = 0 # Reset size to 0
        self.buckets = self.__create_buckets(self.capacity) # Create new buckets with the new capacity

        for bucket in old_buckets: # Traverse through each bucket in the old buckets
            current = bucket.head # Start from the head of the linked list
            while current is not None:
                self.insert(current.key, current.value) # Reinsert each key-value pair into the new buckets
                current = current.next # Move to the next node in the linked list

    def insert(self, key, value):
        index = self.__hash_function(key) # Calculate the index using the hash function
        bucket = self.buckets[index] # Get the bucket at the calculated index
        node = bucket.search(key) # Search for the key in the bucket
        if node is None:
            bucket.add(key, value)
            self.size += 1
        else:
            node.value = value
            print(f"Key '{key}' updated with new value: {value}")
            
        load_factor = self.size / self.capacity
        print(f"Current load factor: {load_factor:.2f}")
        if load_factor > 0.75:  # If load factor exceeds 0.75
            self.__rehash()
        
        
    def get(self, key):
        index = self.__hash_function(key) # Calculate the index using the hash function
        bucket = self.buckets[index] # Get the bucket at the calculated index
        value = bucket.search(key) # Search for the key in the bucket

        if value is not None:
            return value
        else:
            return "Key not found"

    def remove(self, key):
        index = self.__hash_function(key)
        bucket = self.buckets[index]
        if bucket.delete(key):
            self.size -= 1
            print(f"Key '{key}' removed successfully.")
        else:
            print(f"Key '{key}' not found, removal failed.")

    def __len__(self):
        return self.size
    
    def __str__(self):
        for i in range(self.capacity):
            print(f"Bucket {i}:")
            self.buckets[i].traverse()
        return f"Hashmap with {self.size} elements and {self.capacity} buckets."
    
    def traverse(self):
        current = self.head
        while current is not None:
            print(f"{current.key}: {current.value}")
            current = current.next
        print("Traversal complete.")

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.insert(key, value)

    def __delitem__(self, key):
        self.remove(key)
