class HashTableEntry:
    """
    Linked lst hash table key/value pair
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
        if capacity >= 8:
            self.capacity = capacity
        else:
            self.capacity = 8
            raise Exception('The capacity has been set to its minimum: 8.')
        self.lst = [HashTableEntry(None,None)] * self.capacity

    def get_num_slots(self):
        """
        Return the length of the lst you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main lst.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.lst)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        
        return len([x for x in self.lst if x]) / self.capacity



    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        offset_basis = 14695981039346656037
        FNV_prime = 1099511628211

        hash = offset_basis
        for octect in key.encode():

            hash = hash * FNV_prime
            hash = hash ^ octect
        
        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381

        for character in key:
            
            hash = (hash * 33) + ord(character)

        return hash 
        
        


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity
        

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked lst Chaining.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        if  not self.lst[index]:

            self.lst[index] = HashTableEntry(key,value)
        
        else:

          current = self.lst[index]

          while current:

            if current.key == key:

              current.value = value
              break
            
            current = current.next
          
          prev = self.lst[index]

          self.lst[index] = HashTableEntry(key,value)
          self.lst[index].next = prev

        if self.get_load_factor() > 0.7:

            self.resize(self.capacity * 2)
        




    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)

        if index < self.capacity and self.lst[index]:

            current = self.lst[index]

            if current.key == key:

                if current.next:

                    previous = self.lst[self.hash_index(key)]
                    self.lst[self.hash_index(key)] = self.lst[self.hash_index(key)].next
                    previous.next = None
                    return

                else: 

                    previous = self.lst[self.hash_index(key)]
                    self.lst[self.hash_index(key)] = None
                    previous.next = None
                    return

            while current.next:

                previous = current
                current = current.next

                if current.next:

                    previous.next  = current.next
                    current.next = None
                    return

                else: 

                    previous.next = None
                    return

        else:

            raise Exception('The key was not found.')

        if self.get_load_factor() < 0.2:

            self.resize(int(self.capacity // 2))

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        if index < self.capacity:

            if not self.lst[index]:

                return None

            current = self.lst[index]
            if current.key == key:

              return current.value

            while current.next:

              if current.next.key == key:

                return current.next.value

              current = current.next
            
            return

        else:

          return



    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here

        if new_capacity < 8:

            print('The new capacity has been set to is minimum: 8.')
            new_capacity = 8

        previous_lst = self.lst.copy()
        self.capacity = new_capacity
        self.lst = [None] * self.capacity

        for i in range(len(previous_lst)):

            if previous_lst[i]:

                current = previous_lst[i]

                while current:
                    
                    if current.key:

                        self.put(current.key,current.value)
                    
                    current = current.next


        

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

