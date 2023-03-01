from llist import *
from gencyclic import lst

def llprint(lst, num):
    """print the first num terms of linked list lst"""
    node = lst.head
    while node.next and num >= 0: 
        print(node.val, end= ", ")
        node = node.next
        num -= 1
    print(node.val)

def find_cycle(lst):
    """return the start index and length of the cycle"""
    tortoise = lst.head
    hare = lst.head.next.next
    i = 0 

    while tortoise is not hare: 
        tortoise = tortoise.next
        hare = hare.next.next
        i += 1
    tortoise = tortoise.next
    j = 0
    while tortoise is not hare: 
        tortoise = tortoise.next 
        j += 1
    
    return i, j 


if __name__ == "__main__":

    start, length = find_cycle(lst)
    print(f"Starts at node {str(start)} and cycles {str(length)} items.")
