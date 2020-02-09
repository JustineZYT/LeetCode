class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr1 = l1
        curr2 = l2
        a, b = 0, 0
        i = 1
        while curr1:
            a += curr1.val*i
            curr1 = curr1.next
            i = i*10
        j = 1
        while curr2:
            b += curr2.val*j
            curr2 = curr2.next
            j = j*10
        summ = a+b
        l = list(str(summ))
        res = ListNode(int(l[-1]))
        out = res
        l = l[:-1]
        while l:
            res.next = ListNode(int(l[-1]))
            res = res.next
            l = l[:-1]
        return out