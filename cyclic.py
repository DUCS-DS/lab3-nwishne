from llist import *

def llprint(lst, num):
    """print the first num terms of linked list lst"""
    if lst.head:
        node = lst.head
        print(node.val)
        while node.next:
            node = node.next
            print(node.val)
    else:
        print(lst.head)

def find_cycle(lst):
    """return the start index and length of the cycle"""
    pass


if __name__ == "__main__":

    pass
