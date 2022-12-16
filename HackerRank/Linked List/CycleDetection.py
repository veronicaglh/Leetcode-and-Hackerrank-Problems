# This problem is called Cycle Detection
# You can acccess it here: https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem

# A linked list is said to contain a cycle if any node is visited more 
# than once while traversing the list. Given a pointer to the head of 
# a linked list, the program will determine if it contains a cycle. 
# If it does, it will return 1. Otherwise, return 0.
# For example if  head refers to the list of nodes 1-> 2-> 3->NULL
# The numbers shown are the node numbers, not their data values. 
# There is no cycle in this list so return 0.

#!/bin/python3

import math
import os 
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node
        
def has_cycle(head):
    if (head == None):
        return 0

    else:
        slow = head
        fast = head.next
        while (slow != fast) :
            if (fast == None or fast.next == None):
                return 0
            else:
                slow = slow.next
                fast = fast.next.next
        return 1
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        extra = SinglyLinkedListNode(-1);
        temp = llist.head;

        for i in range(llist_count):
            if i == index:
                extra = temp

            if i != llist_count-1:
                temp = temp.next

        temp.next = extra

        result = has_cycle(llist.head)

        fptr.write(str(int(result)) + '\n')

    fptr.close()
