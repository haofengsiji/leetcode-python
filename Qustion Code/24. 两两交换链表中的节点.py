# method_1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        i = head
        count = 0
        while i != None:
            if count %2 == 0:
                p1 = i
                i = i.next
            elif count == 1:
                p2 = i
                i = i.next
                # swap
                p2.next = p1
                p1.next = i
                head = p2
                # helper
                helper = p1
            else:
                p2 = i
                i = i.next
                # swap
                helper.next = p2
                p2.next = p1
                p1.next = i
                # helper
                helper = p1
            count +=1    
        return head

# method_2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         dummy = ListNode(0)
#         dummy.next = head

#         prev_node = dummy

#         while head and head.next:
#             first_node = head
#             second_node = head.next

#             # 交换
#             prev_node.next = second_node
#             first_node.next = second_node.next
#             second_node.next = first_node

#             # 重新初始化节点
#             head = first_node.next
#             prev_node = first_node
#         return dummy.next

# # method_3
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         # 归
#         if not head or not head.next:
#             return head
#         # 递
#         first_node = head
#         second_node = head.next

#         first_node.next = self.swapPairs(second_node.next)
#         second_node.next = first_node

#         return second_node