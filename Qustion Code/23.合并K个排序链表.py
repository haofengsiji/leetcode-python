# method_1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        n = len(lists)
        interval = 1
        while interval < n:
            for i in range(0,n-interval,interval*2):
                lists[i] = self.merge(lists[i],lists[i+interval])
            interval *=2
        return lists[0] if n > 0 else None

    
    def merge(self,left,right):
        dummy = ListNode(0)
        p = dummy
        while left != None and right != None:
            if left.val < right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next
            p = p.next
        if left == None: p.next = right
        if right == None: p.next = left

        return dummy.next  