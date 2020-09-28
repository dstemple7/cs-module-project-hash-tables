class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.data = [None for i in range(capacity)]
        self.size = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.size / self.get_num_slots()

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        Implement this, and/or DJB2.
        """

        # Your code here

        # Constants
        # FNV_prime = 1099511628211
        # offset_basis = 14695981039346656037

        # #FNV-1a Hash Function
        # hash = offset_basis + key

        # for char in string:
        #     hash = hash * FNV_prime
        #     hash = hash ^ ord(char)
        # return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381

        for i in key:
            hash = ((hash << 5) + hash) + ord(i)
        
        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # Your code here

        # index = hash_index(value)
        # HashTable[index] = HashTableEntry(key, value)

        # pool = self.hash_index(key)

        # if self.data[pool] is None:
        #     self.data[pool] = HashTableEntry(key, value)
        #     self.size += 1
        
        # else:
        #     current = self.data[pool]

        #     while current.next is not None and current.key != key:
        #         current = current.next

        #     if current.key == key:
        #         current.value = value
            
        #     else:
        #         current.next = HashTableEntry(key, value)
        #         self.size += 1

        i = self.hash_index(key)
        self.data[i] = HashTableEntry(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # Your code here
        # pool = self.hash_index(key)

        # current = self.data[pool]
        
        # if current is None:
        #     print('Not found')
        # elif current.key == key:
        #     self.data[pool] = current.next
        #     self.size -= 1
        # else:
        #     while current.next is not None and current.next.key != key:
        #         current = current.next

        #     if current.next.key == key:
        #         current.next = current.next.next
        #         self.size -= 1
        #     else:
        #         print('Not found')
        x = None
        self.put(key, x)

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # Your code here

        # index = hash_index(key)
        # HashTableEntry = HashTable[index]
        # return HashTableEntry.value


    # def resize(self, new_capacity):
    #     """
    #     Changes the capacity of the hash table and
    #     rehashes all key/value pairs.

    #     Implement this.
    #     """
    #     # Your code here

        # pool = self.hash_index(key)

        # if self.data[pool] is not None:
        #     current = self.data[pool]

        #     while current is not None and current.key != key:
        #         current = current.next

        #     if current:
        #         return current.value
        #     else:
        #         return None
        
        # else:
        #     return None
        i = self.hash_index(key)
        current = self.data[i]
        return current.value

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
