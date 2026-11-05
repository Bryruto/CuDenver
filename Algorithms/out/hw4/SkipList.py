import math
import random
#skiplist class 
class Brycen_SkipList:
    # in python i think the best way to do this would be a hashmap

    def __init__(self,max_elements):
        self.skiplist = {}
        self.element_count = 0
        self.height = math.ceil(math.log2(max_elements))
        
    #methods 
    def search(self,keys)->bool:
        #i did this because you want after all searchs and inserts time
        for key in keys:
            index = 0
            #search all levels backward 
            for level in range(self.height-1,-1,-1):
                # if the level is in there 
                if level in self.skiplist: 
                    for num in range(index,len(self.skiplist[level])):
                        #i forgot about this My code is about to get very unreadable 
                        if self.skiplist[level][num] == key: return True
                        elif self.skiplist[level][num] > key: break
                        index+=1
        return False

    def insert(self,values):
        for value in values:
            #get a random level
            level = 1 # always insert at 0 
            while level < self.height and random.randint(0,1) == 1:
                level +=1
            
            # add value to all levels till at it's level
            for i in range(level):
                if i in self.skiplist:
                    self.skiplist[i].append(value)
                    #must sort after because a skiplist is sorted 
                    self.skiplist[i].sort()
                    
            #if not in hashmap add it  
                else:
                    self.skiplist[i] = [value]
