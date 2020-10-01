class HashTableEntry:
    """Linked List hash table key/value pair"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class HashTable:
    """A hash table that with `capacity` buckets that accepts string keys.Implement this."""

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.data = [None for i in range(capacity)]
        self.size = 0

    def get_num_slots(self):
        """Return the length of the list you're using to hold the hash table data. (Not the number of items stored in the hash table, but the number of slots in the main list.) One of the tests relies on this. Implement this."""
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """Return the load factor for this hash table. Implement this."""
        # Your code here
        return self.size / self.get_num_slots()

    def djb2(self, key):
        """DJB2 hash, 32-bit. Implement this, and/or FNV-1."""
        # Your code here
        hash = 5381

        for i in key:
            hash = ((hash << 5) + hash) + ord(i)
        
        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """Take an arbitrary key and return a valid integer index between within the storage capacity of the hash table."""
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """Store the value with the given key. Hash collisions should be handled with Linked List Chaining. Implement this. """
        # Your code here

        i = self.hash_index(key)

        if self.data[i] is None:
            self.data[i] = HashTableEntry(key, value)
            self.size += 1

            if self.get_load_factor() > .7:
                self.resize(self.capacity * 2)
        
        else:
            cur = self.data[i]

            while cur.next is not None and cur.key != key:
                cur = cur.next

            if cur.key == key:
                cur.value = value
            else:
                cur.next = HashTableEntry(key, value)
                self.size += 1

                if self.get_load_factor() > .7:
                    self.resize(self.capacity * 2)

    def delete(self, key):
        """Remove the value stored with the given key. Print a warning if the key is not found. Implement this."""
        # Your code here
        i = self.hash_index(key)
        cur = self.data[i]

        if cur is None:
            print('not found')
        elif cur.key == key:
            self.data[i] = cur.next
            self.size -= 1
        else:
            while cur.next is not None and cur.netxt.key != key:
                cur = cur.next

            if cur.next.key == key:
                cur.next = cur.next.next
                self.size -= 1
            else:
                print('not found')

    def get(self, key):
        """Retrieve the value stored with the given key. Returns None if the key is not found. Implement this."""
        # Your code here
        i = self.hash_index(key)

        if self.data[i] is not None:
            cur = self.data[i]

            while cur is not None and cur.key != key:
                cur = cur.next
            
            if cur:
                return cur.value
            else:
                return None
        else:
            return None

    def resize(self, new_capacity):
        """Changes the capacity of the hash table and rehashes all key/value pairs. Implement this."""
        # Your code here
        self.capacity = new_capacity
        new_list = [None for i in range(new_capacity)]

        for linked_list in self.data:
            cur = linked_list

            while cur is not None:
                i = self.hash_index(cur.key)

                if new_list[i] is None:
                    new_list[i] = HashTableEntry(cur.key, cur.value)
                else:
                    new_cur = new_list[i]

                    while new_cur.next is not None:
                        new_cur = new_cur.next

                    new_cur.next = HashTableEntry(cur.key, cur.value)                   

                cur = cur.next

        self.data = new_list

if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
