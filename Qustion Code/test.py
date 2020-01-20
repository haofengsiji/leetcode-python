class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(None)
        while True:
            if l1.val == None or l2.val == None:
                dummy.next = l1.val
                l1.next = l2.val
                break
            elif l1.val < l2.val:
                dummy.next = l1.val
                l1 = l1.next
            else:
                dummy.next = l2.val
                l2 = l2.next
        return dummy.next

if __name__ == "__main__":
    s = Solution()

    print(s.mergeTwoLists(ListNode([1,2,3]),ListNode([1,2,3])))