# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self.link2num(l1)
        num2 = self.link2num(l2)
        num3 = num1 + num2
        l3 = self.num2link(num3)
        return l3
    
    #  Convert link to num
    def link2num(self,l: ListNode) -> int:
        num = 0 
        count = 0
        while l:
            num += l.val*10**count
            count += 1
            l = l.next
        return num

    # Convert num to link
    def num2link(self,num:int) -> ListNode:
        l = ListNode(None)
        tem_l = ListNode(None)
        while True:
            rem = num%10
            num = num//10
            if tem_l.val == None:
                tem_l = ListNode(rem)
                l = tem_l
            else:
                tem_l.next = ListNode(rem)
                tem_l = tem_l.next
            if num == 0:
                break
        return l
