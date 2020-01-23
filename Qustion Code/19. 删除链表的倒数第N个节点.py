# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = head
        ans = head
        delay = n+1
        count = 0
        
        while p != None:
            count +=1
            p = p.next
            if delay > 0:
                delay -=1
            else:
                ans = ans.next
        # 头部
        if count == n:
            head = head.next
            return head
        # 尾部
        elif n == 1:
            ans.next = None
            return head
        # 中间
        else:
            ans.next = ans.next.next
            return head