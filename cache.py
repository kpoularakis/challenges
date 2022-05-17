
'''
Design  a data structure for cache. It should support the following operations: get, put and delete.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should randomly invalidate an item. Ensure that each element has equal probability to be eliminated. No duplicates. 
delete(key) - Delete the value based on the key.
'''

#my solution is to maintain two data structures:
#1) an array of size equal to the capacity of the cache where  myarray[index] = key
#2) a hashmap where myhash[key] = (value, index)
#the get(key) operation takes O(1) time ( a simple hashmap lookup that returns the value from the accessed tuple (value,index) )
#the put(key, value) operation takes O(1) time ( if cache is full, it chooses a random integer index, swaps the myarray[index] with the last element myarray[-1] and then deletes myarray[-1]. Finally, it deletes the myarray[-1] from hashmap )
#the delete(key) operation takes O(1) time ( a simple hashmap lookup that returns the index from the accessed tuple (value,index), then similarly to the above it swaps myarray[index] with myarray[-1], deletes myarray[-1], and finally deletes key from hashmap )
#the main idea here is that by swapping the random element with the last in the array, then I can delete in O(1) time (instead of O(N) that is the typical time in arrays)
#The use of two data structures seems necessary  to achieve O(1) time for all three operations

import random

class RandomCache:
    def __init__(self,capacity):
        self.myhash = {}                    #first data structure: hash for O(1) time access of key values 
        self.capacity = capacity
        self.myarray = [0]*self.capacity    #second data stucture: array for O(1) time random selection of key         
        self.utilization = 0
        
    def put(self, key, value):
        if key in self.myhash:                              #if key is already in myhash: just update its value
            self.myhash[key][0] =  value
        else:                                               #otherwise:
            index = self.utilization                             #find the next available array index to store the new key
            if index == self.capacity:                           #if array is full
                random_index = random.randint(0, index-1)        #pick a random index inside the array:  O(1) time
                if random_index != index - 1:                    #if the picked index is not the last in the array
                    self.myarray[random_index], self.myarray[index - 1] = self.myarray[index - 1], self.myarray[random_index] #swap the picked index with the last in the array
                    self.myhash[ self.myarray[random_index] ][1] = random_index                                               #update the index of the other swapped element in the hashmap 
                del self.myhash[ self.myarray[index - 1] ]      #finally, delete the last index: O(1) time
                self.utilization -= 1
                index = self.utilization 
            self.myarray[index] =  key                          #store the new key in both the array and hashmap
            self.myhash[key] = [ value, index ]
            self.utilization += 1
    
    def get(self, key):                                     #O(1) time since it is a hashmap lookup
        if key not in self.myhash: 
            return -1
        return self.myhash[key][0]

    def delete(self, key):
        if key not in self.myhash: 
            return -1
        index = self.myhash[ key ][1]           #find the index in the array of the key to be deleted
        if index != self.capacity - 1:          #if this index is not the last in the array
            self.myarray[index], self.myarray[self.capacity - 1] = self.myarray[self.capacity - 1], self.myarray[index] #swap with the last index
            self.myhash[ self.myarray[index] ][1] = index                                                               #update the index of the non-deleted swapped element 
        del self.myhash[ key ]                  #finally, delete the key from myhash 
        self.utilization -= 1

#Test cases
mycache =  RandomCache(2)

mycache.put(1,10)
print(mycache.myhash)

mycache.put(2,20)
print(mycache.myhash)

mycache.put(3,30)
print(mycache.myhash)

print(mycache.get(1))

mycache.delete(1)

print(mycache.myhash)
print(mycache.get(1))

mycache.put(1,100)
print(mycache.myhash)

