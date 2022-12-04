# This problem is called 707. Design Linked List
# You can access it here: https://leetcode.com/problems/design-linked-list/

# The program will implement the MyLinkedList class:
# - MyLinkedList() Initializes the MyLinkedList object.
# - int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
# - void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
# - void addAtTail(int val) Append a node of value val as the last element of the linked list.
# - void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
# - void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
# For example: 
# If Input: 
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# Then the output will be: 
# [null, null, null, null, 2, null, 3]
# Because:
# - MyLinkedList myLinkedList = new MyLinkedList();
# - myLinkedList.addAtHead(1);
# - myLinkedList.addAtTail(3);
# - myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
# - myLinkedList.get(1);              // return 2
# - myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
# - myLinkedList.get(1);              // return 3

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None


class MyLinkedList:
  def __init__(self):
    self.length = 0
    self.dummy = ListNode(0)

  def get(self, index: int) -> int:
    if index < 0 or index >= self.length:
      return -1
    curr = self.dummy.next
    for _ in range(index):
      curr = curr.next
    return curr.val

  def addAtHead(self, val: int) -> None:
    curr = self.dummy.next
    self.dummy.next = ListNode(val)
    self.dummy.next.next = curr
    self.length += 1

  def addAtTail(self, val: int) -> None:
    curr = self.dummy
    while curr.next:
      curr = curr.next
    curr.next = ListNode(val)
    self.length += 1

  def addAtIndex(self, index: int, val: int) -> None:
    if index > self.length:
      return
    curr = self.dummy
    for _ in range(index):
      curr = curr.next
    temp = curr.next
    curr.next = ListNode(val)
    curr.next.next = temp
    self.length += 1

  def deleteAtIndex(self, index: int) -> None:
    if index < 0 or index >= self.length:
      return
    curr = self.dummy
    for _ in range(index):
      curr = curr.next
    temp = curr.next
    curr.next = temp.next
    self.length -= 1