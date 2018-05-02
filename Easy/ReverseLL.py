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
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        nodeList = []

        while head.next is not None:
            nodeList.append(head.val)
            head = head.next
        nodeList.append(head.val)

        rev = node = ListNode(nodeList[::-1][0])

        for li in nodeList[::-1][1:]:
            node1 = ListNode(li)
            node.next = node1
            node = node1

        return rev

        # prev = ListNode(head.val)
        # node = self.revLL(head.next, prev)
        # return node

    def revLL(self, head, prev):
        if head is None:
            return prev

        node = ListNode(head.val)
        node.next = prev
        head = head.next
        prev = node
        return self.revLL(head, prev)

def listToNode(li):
    node = ListNode(li[0])
    for l in li[1:]:
        node.insert(l)
    return node

iList1 = [1, 2, 3]
# iList2 = [3, 4, 5]
inode1 = listToNode(iList1)
# inode2 = listToNode(iList2)
display(inode1)
s = Solution()
display(s.reverseList(inode1))
