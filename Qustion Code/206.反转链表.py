# method_1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 归
        if head == None or head.next == None: return head
        # 递
        p = self.reverseList(head.next)
        # 交换当前head 和 head.next
        head.next.next = head
        head.next = None
        return p

# method_2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur != None:
            # change the link
            temp = cur.next
            cur.next = pre

            pre = cur
            cur = temp
        return pre