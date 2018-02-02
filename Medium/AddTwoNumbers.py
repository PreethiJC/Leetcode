# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    '''
    These methods are helpful in creating inputs. I will leave it to you to make some minor modifications if you 
    ever need to run this program here again.
    '''
    def getNext(self):
        return self.next

    def setNext(self, node):
        self.next = node

    def printNode(self):
        node = self
        while node is not None:
            print node.val
            node = node.next


class Solution(object):
    def makeListNode(self, lst, node):
        for l in lst:
            n = ListNode(l)
            node.next = n
            node = node.next

    def lstToNum(self, lst):
        times = len(lst) - 1
        places = pow(10, times)
        num = 0
        for l in lst:
            num += l * places
            places /= 10

        return num

    def nodeToLst(self, node):
        lst = []
        while node is not None:
            lst.append(node.val)
            node = node.next
        return lst[::-1]

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = self.lstToNum(self.nodeToLst(l1))
        num2 = self.lstToNum(self.nodeToLst(l2))
        sum = num1 + num2
        sumLst = map(int, str(sum))[::-1]
        sumNode = ListNode(sumLst[0])
        self.makeListNode(sumLst[1:], sumNode)
        return sumNode


'''
Partially correct answer that is supposedly faster:
'''
# def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#     carry = 0
#     sum = l1.val + l2.val + carry
#     l3 = ListNode(sum%10)
#     carry = sum/10
#     if l1.next is not None and l2.next is not None:
#         self.addRecursive(carry, l1.next, l2.next, l3)
#     else:
#         if carry != 0:
#             l3.setNext(ListNode(carry))
#     l3.printNode()
#
# def addRecursive(self, carry, l1, l2, l3):
#     if l1.next is not None and l2.next is not None:
#         sum = l1.val + l2.val + carry
#         carry = sum / 10
#         l3.setNext(ListNode(sum % 10))
#         self.addRecursive(carry, l1.next, l2.next, l3.getNext())
#     else:
#         sum = l1.val + l2.val + carry
#         carry = sum / 10
#         l3.setNext(ListNode(sum%10))
#         if carry != 0:
#             l3.getNext().setNext(ListNode(carry))
#         # l3.printNode()
#         return l3

'''
Example for creating the input. Mind you the methods have been moved between classes. Correct it!
'''
# lst1 = [5]
# lst2 = [5]
# l1 = ListNode(lst1[0])
# l2 = ListNode(lst2[0])
#
#
# def makeListNode(lst, node):
#     for l in lst:
#         n = ListNode(l)
#         node.setNext(n)
#         node = node.getNext()
#
#
# makeListNode(lst1[1:], l1)
# makeListNode(lst2[1:], l2)
# # l1.printNode()
# # l2.printNode()
# print(l1.nodeToLst())
# soln = Solution()
# soln.addTwoNumbers(l1, l2)
