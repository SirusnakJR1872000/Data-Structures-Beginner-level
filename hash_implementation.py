# lets first create a simple class Pair for our hash which would have the key and the value
class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val

# now we will define a hash map with size 0 that is the number of elements 
# and capacity 2 indicating that for now we can only store upto 2 elements
class HashMap:
    def __init__(self):
        self.size = 0
        self.capacity = 2
        self.map = [None, None]

 # now we will compute a hash key for a given value   
    def hash(self, key):
        # we will use a variable to sum up the ASCII values 
        index = 0
        # now we need a variable to that will iterate over each character in the key
        for c in key:
            # ord() converts the character into ASCII value and we will keep on adding it
            index += ord(c)
        # after taking the sum we know that the sum will be out of bounds
        # so we will take modulus with respect to the capacity so that the result will be in bounds
        return index % self.capacity
    
    # suppose we want to retrive an element from the hash map
    def get(self, key):
        # we will call the hash function which assigned the index 
        index = self.hash(key)

        # so we will iterate through the map until the index is not Nonr
        while self.map[index] != None:
            # if we find the matching key we will return the val associated with the key
            if self.map[index].key == key:
                return self.map[index].val
            # if it doesn't match we will increment the pointer 
            index += 1
            # we still need to make sure that the index is within the bounds 
            index = index % self.capacity
        return None
    
    # suppose we want to insert/update a value in the hashmap 
    def put(self, key, val):
        # we will call the hash function which assigned the index 
        index = self.hash(key)

        # so we will run the loop until the condition is fulfilled
        while True:
            # we need to first check if the index at which the element will be inserted is empty or not
            if self.map[index] == None:
                # if the condition is satisfied then we insert by calling the Pair()
                self.map[index] = Pair(key, val)
                # since we have inserted we need to increase the size
                self.size += 1
                # now we know need to check if the hash is half full so that we can increase the size to avoid collisions
                if self.size >= self.capacity // 2:
                    # for this we will call the rehash() which will resize the hash
                    self.rehash()
                return
            # now if the slot is not empty 
            # then we check if the key matches with the given key
            # if the match is found then the value needs to be updated
            elif self.map[index].key == key:
                self.map[index].val = val
                return
            
            # if the slot does not match then we increment the index pointer    
            index += 1
            # now we just make sure that the index does not go out of bounds
            index = index % self.capacity

    # if the hash is half full as per the condition then we just resize the hash 
    def rehash(self):
        # we will increase the capacity to twice of the original
        self.capacity = 2 * self.capacity
        # we then create a empty list to insert the old values
        newMap = []
        # we ill keep on adding the elements to the new list
        for i in range(self.capacity):
            newMap.append(None)
        
        # we need to store the keyvalue pair before rehashing 
        oldMap = self.map
        # we then pass them to the new map created
        self.map = newMap
        # then we just set the size to 0 initially 
        self.size = 0
        # now we need to go through each pair in the map
        for pair in oldMap:
            # if a pair is not None
            if pair:
                self.put(pair.key, pair.val)

    # suppose we want to remove a value from the map
    def remove(self, key):
        # we will search if the key exists or not
        if not self.get(key):
            return
        
        # now we calculate the hash index by calling the hash function
        index = self.hash(key)
        # we will run the loop till the condition is True
        while True:
            # we will check if the key matches 
            if self.map[index].key == key:
                # if the match is found then we set that slot to None effectively removing it 
                self.map[index] = None
                # since we removed a value we reduce the size by 1
                self.size -= 1
                return
            # if a match is not found then the index value is incremented to look at next position
            index += 1
            # if we go out of bounds then we calcualate the mod value
            index = index % self.capacity

    # finally lets try printing the hash map
    def print(self):
        # we will run through each pair
        for pair in self.map:
            # if pair exist then we print
            if pair:
                print(pair.key, pair.val)