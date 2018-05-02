# Definition for singly-linked list.
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

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node = head = ListNode(0)
        node = self.recursiveFn(l1, l2, node)
        display(node)
        return head.next


    def recursiveFn(self, l1, l2, node):
        if l1 is None and l2 is not None:
            node.next = l2
            return node
        elif l2 is None and l1 is not None:
            node.next = l1
            return node
        elif l1 is None and l2 is None:
            node.next = None
            return node
        print(l1.val, l2.val)
        if l1.val <= l2.val:
            minVal = l1.val
            l1 = l1.next
        else:
            minVal = l2.val
            l2 = l2.next

        node1 = ListNode(minVal)
        node.next = node1


        return self.recursiveFn(l1, l2, node1)

def listToNode(li):
    node = ListNode(li[0])
    for l in li[1:]:
        node.insert(l)
    return node

iList1 = [1, 2, 3]
iList2 = [3, 4, 5]
inode1 = listToNode(iList1)
inode2 = listToNode(iList2)
# display(inode1)
s = Solution()
display(s.mergeTwoLists(inode1, inode2))




