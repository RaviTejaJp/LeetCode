# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first,flag1,flag2,val1,val2,carry = 0,0,0,l1.val,l2.val,0
        l3 = ListNode()
        result = l3
        while flag1==0 or flag2==0:
            if first == 1:
                l3.next = ListNode()
                l3 = l3.next
            else:
                first = 1
            val3 = val1+val2+carry
            rem = int(val3 % 10)
            if val3>9:
                carry = 1
            else:
                carry = 0
            l3.val = rem
            if l1.next == None:
                val1 = 0
                flag1 = 1
            else:
                l1 = l1.next
                val1 = l1.val
            if l2.next == None:
                val2 = 0
                flag2 = 1
            else:
                l2 = l2.next
                val2 = l2.val
        if carry == 1:
            l3.next=ListNode()
            l3 = l3.next
            l3.val = carry
        else:
            l3.next=None
        return result
