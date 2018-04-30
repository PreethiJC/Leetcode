# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
#       self.prevNode = self
#
#
#     def insert(self, x):
#         newList = ListNode(x)
#         self.prevNode.next = newList
#         self.prevNode = newList
#
# def lenLL(node):
#     count = 0
#     while node.next is not None:
#         count += 1
#         node = node.next
#     count += 1
#     return count
#
#
# def display(node):
#     while node.next is not None:
#         print str(node.val) + " ->",
#         node = node.next
#     print str(node.val)


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        lists = [x for x in lists if x is not None]
        if not lists:
            return []
        minVal, lists = self.minNode(lists)
        head = node = ListNode(minVal)
        while lists:
            minVal, lists = self.minNode(lists)
            node.next = ListNode(minVal)
            node = node.next
        return head

    def minNode(self, lists):
        min = lists[0].val
        i = j = 0
        for node in lists:
            if node.val <= min:
                min = node.val
                i = j
            j += 1

        if lists[i].next is None:
            lists.pop(i)
        else:
            lists[i] = lists[i].next

        return min, lists


