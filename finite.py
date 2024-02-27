from llist import LList, Node, append


def length(lst):
    """return the length of a finite linked list"""
    count = 0
    if lst.head:
        node = lst.head
        count = 1
        while node.next:
            count += 1
            node = node.next
    else:
        count = 0
    print(count)

def llprint(lst):
    """print a finite linked list"""
    
    if lst.head:
        node = lst.head
        print(node.val)
        while node.next:
            node = node.next
            print(node.val)
    else:
        print(lst.head)

if __name__ == "__main__":

    llist = LList()
    append(llist, Node(1))
    append(llist, Node(2))
    append(llist, Node(4))
    append(llist, Node(8))
    append(llist, Node(16))
    append(llist, Node(32))
    append(llist, Node(64))
    append(llist, Node(128))
    append(llist, Node(256))
    append(llist, Node(512))
    print("This works right")
    length(llist)
    print('List:')
    llprint(llist)