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

# method_2:暴力法 还挺快的
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nums = []
        for l in lists:
            while l != None:
                nums.append(l.val)
                l = l.next

        points = ListNode(0)
        p = points
        for num in sorted(nums):
            cur = ListNode(num)
            p.next = cur
            p = cur
        return points.next

# method_3: 优先队列，有点慢
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from  queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        q = PriorityQueue()
        # 向优先队列里放置头节点的值和节点
        for i,l in enumerate(lists):
            if l:
                # 多加一个index是为了防止比较节点，节点无法比较
                q.put((l.val,i,l))
        prehead = ListNode(0)
        p = prehead
        while not q.empty():
            # 取出头节点最小的值，加入输出链表
            val, index, node = q.get()
            p.next = ListNode(val)
            p = p.next
            node = node.next
            if node:
                q.put((node.val,index,node))

        return prehead.next