class Hashmaps:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.slots = [None] * self.capacity
        self.values = [None] * self.capacity

    def hash_function(self, key):
        return abs(hash(key)) % self.capacity

    def rehash(self, old_hash_value):
        return (old_hash_value + 1) % self.capacity
    
    def insert(self, key, value):
        hash_value = self.hash_function(key)
        initial_index = hash_value
        
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.values[hash_value] = value
            self.size += 1
        else:
            if self.slots[hash_value] == key:
                self.values[hash_value] = value

            new_hash_value = self.rehash(hash_value)
            while self.slots[new_hash_value] is not None and self.slots[new_hash_value] != key:
                new_hash_value = self.rehash(new_hash_value)
                if new_hash_value == initial_index:
                    raise Exception("Hashmap is full")
            
            if self.slots[new_hash_value] is None:
                self.slots[new_hash_value] = key
                self.values[new_hash_value] = value
            else:
                self.values[new_hash_value] = value
                
    def get(self, key):
        initial_index = self.hash_function(key)
        current_position = initial_index

        while self.slots[current_position] is not None:
            if self.slots[current_position] == key:
                return self.values[current_position]
            current_position = self.rehash(current_position)
            if current_position == initial_index:
                return "Key not found, hashmap is full"
            
        return "Key not found, slot is empty"
    
    def delete(self, key):
        initial_index = self.hash_function(key)
        current_position = initial_index

        while self.slots[current_position] is not None:
            if self.slots[current_position] == key:
                self.slots[current_position] = None
                self.values[current_position] = None
                self.size -= 1
                print(f"Key '{key}' deleted successfully.")
            current_position = self.rehash(current_position)
            if current_position == initial_index:
                break
        
        print(f"Key '{key}' not found, nothing to delete.")


    def __setitem__(self, key, value):
        self.insert(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __str__(self): # String representation of the hashmap, prints all key-value pairs
        items = []
        for i in range(self.capacity):
            if self.slots[i] is not None:
                items.append(f"{self.slots[i]}: {self.values[i]}")
        return "{" + ", ".join(items) + "}"