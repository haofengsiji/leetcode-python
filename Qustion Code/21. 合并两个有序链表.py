# method_1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        p = dummy
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1 == None: p.next = l2
        if l2 == None: p.next = l1
        return dummy.next

# # method_2
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         if l1 == None: return l2
#         if l2 == None: return l1
#         if l1.val < l2.val:
#             l1.next = self.mergeTwoLists(l1.next,l2) # l1小，所以将此链表取下来
#             return l1 # 将小的取下来接回去
#         else:
#             l2.next = self.mergeTwoLists(l1,l2.next)
#             return l2