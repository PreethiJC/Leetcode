class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prevNode = self

    def insert(self, x):
        newNode = ListNode(x)
        self.prevNode.next = newNode
        self.prevNode = newNode

def display(node):
    while node.next is not None:
        print str(node.val) + " ->",
        node = node.next
    print str(node.val)


def listToNode(li):
    node = ListNode(li[0])
    for l in li[1:]:
        node.insert(l)
    return node

def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    llStr = []
    while head.next is not None:
        llStr.append(head.val)
        head = head.next
    llStr.append(head.val)
    if llStr == llStr[::-1]:
        return True
    return False

iList1 = [1, 2, 3, 4, 5]
inode1 = listToNode(iList1)
print(isPalindrome(inode1))
iList1 = [1, 2, 1]
inode1 = listToNode(iList1)
print(isPalindrome(inode1))
iList1 = [-129, -129]
inode1 = listToNode(iList1)
print(isPalindrome(inode1))
