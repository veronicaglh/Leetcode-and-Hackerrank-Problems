# This problem is called 460. LFU Cache
# You can access it here: https://leetcode.com/problems/lfu-cache/

# The program will design and implement a data structure for a Least Frequently Used (LFU) cache.
# Implement the LFUCache class:
# - LFUCache(int capacity) Initializes the object with the capacity of the data structure.
# - int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
# - void put(int key, int value) Update the value of the key if present, or inserts the key if not 
# - already present. When the cache reaches its capacity, it should invalidate and remove the least 
# - frequently used key before inserting a new item. For this problem, when there is a tie 
# - (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
# To determine the least frequently used key, a use counter is maintained for each key in the cache. 
# The key with the smallest use counter is the least frequently used key.
# When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). 
# The use counter for a key in the cache is incremented either a get or put operation is called on it.
# For example if input: ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
# The the output will be: [null, null, null, 1, null, -1, 3, null, -1, 3, 4]

class Node:
  def __init__(self, key, val):
    self.key = key
    self.val = val
    self.freq = 1
    self.prev = self.next = None

class DLinkedLikst:
  def __init__(self):
    self.dummyHead=Node(None, None)
    self.dummyTail=Node(None, None)
    self.dummyHead.next=self.dummyTail
    self.dummyTail.prev=self.dummyHead
    self._size=0
    
  def __len__(self):
      return self._size
    
  def append(self,node):
    node.next=self.dummyHead.next
    node.prev=self.dummyHead
    self.dummyHead.next.prev=node
    self.dummyHead.next=node
    self._size+=1
  
  def popLRU(self):
    if self._size==0: return None
    else:
      LRUnode=self.dummyTail.prev
      self.dummyTail.prev=LRUnode.prev
      LRUnode.prev.next=self.dummyTail
      self._size-=1
      return LRUnode
    
  def pop(self,givenNode):
    if self._size==0: return None
    else:
      givenNode.prev.next=givenNode.next
      givenNode.next.prev=givenNode.prev
      self._size-=1
      return givenNode
    

class LFUCache: 
    def __init__(self, capacity: int):
      self._cap=capacity
      self._node={} #key = key, val = node
      self._freq=collections.defaultdict(DLinkedLikst) #key=freq val=DLinkedList
      self.min_freq=0 # for pop off LFU
      self._size=0
   
    def update(self, key: int) -> None:
      aNode=self._node[key]
      aFreq=aNode.freq
      oldDLinkedList=self._freq[aFreq]
      oldDLinkedList.pop(aNode)

      if self.min_freq==aFreq and not self._freq[aFreq]:self.min_freq+=1

      aNode.freq+=1
      newDLinkedList=self._freq[aNode.freq]
      newDLinkedList.append(aNode)
      
    
    def get(self, key: int) -> int:
      if self._node.get(key)!=None:
        self.update(key)       
        return self._node[key].val 
      else: return -1
      
      
    def put(self, key: int, value: int) -> None:
      if self._cap==0: return
      
      if self._node.get(key)!=None:
        self._node[key].val=value
        self.update(key)
      else:
        if self._size==self._cap:
          LRU=self._freq[self.min_freq].popLRU()
          self._size-=1
          self._node.pop(LRU.key)
          
        newNode=Node(key,value)
        self._node[key]=newNode
        self._freq[1].append(newNode)
        self.min_freq=1
        self._size+=1
        
      
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
