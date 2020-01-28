# method_1
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        prehead = ListNode(-1)
        prehead.next = head
        p = prehead

        p_list = [None for _ in range(k)]
        while True:
            # 构建前驱节点
            prenode = p
            # 构建交换节点
            for i in range(k):
                if p == None:
                    break
                p = p.next
                p_list[i] = p
            if p == None:
                break
            # 翻转
            prenode.next = p_list[k-1]
            p_list[0].next = p_list[k-1].next
            for i in range(k-1,0,-1):
                p_list[i].next = p_list[i-1]
            p = p_list[0]
        return prehead.next
# method_2
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        count = 0
        cur = head
        while cur != None and count != k:
            count +=1
            cur = cur.next
        # 递
        if count == k:
            cur = self.reverseKGroup(cur,k)
            while count:
                tmp = head.next
                head.next = cur
                cur = head
                head = tmp
                count -=1
            head = cur
        # 归（递和归的return是一样的就合在一起了）
        return head