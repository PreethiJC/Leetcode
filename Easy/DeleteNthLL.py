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

def sizeLL(node):
    count = 1
    while node.next is not None:
        count += 1
        node = node.next
    return count

def listToNode(li):
    node = ListNode(li[0])
    for l in li[1:]:
        node.insert(l)
    return node

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node = head
        i = 1
        lSize = sizeLL(head)
        nNode = lSize - n
        if lSize == 1 or nNode == 0:
            return head.next

        while node is not None:
            if i == nNode:
                node.next = node.next.next
                break
            i+=1
            node = node.next

        return head


        # while i < n:
        #     lastPtr = lastPtr.next
        #     i += 1
        # # print lastPtr.val
        # if lastPtr is None:
        #     head = None
        #     return head
        # while lastPtr.next is not None:
        #     lastPtr = lastPtr.next
        #     firstPtr = firstPtr.next
        # firstPtr.next = firstPtr.next.next
        # if firstPtr.next is not None:
        #     firstPtr.val = firstPtr.next.val
        #     firstPtr.next = firstPtr.next.next
        # else:
        #     firstPtr = firstPtr.next
        return head

s = Solution()
iList1 = [1, 2, 3, 4, 5]
inode1 = listToNode(iList1)
# display(inode1)
display(s.removeNthFromEnd(inode1, 2))
iList1 = [1]
inode1 = listToNode(iList1)
# display(s.removeNthFromEnd(inode1, 1))
iList1 = [1, 2]
inode1 = listToNode(iList1)
# display(inode1)
display(s.removeNthFromEnd(inode1, 2))
iList1 = [1, 2, 3]
inode1 = listToNode(iList1)
# display(inode1)
display(s.removeNthFromEnd(inode1, 1))