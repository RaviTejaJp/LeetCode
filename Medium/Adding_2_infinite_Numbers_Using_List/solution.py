# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_current_node = ListNode()
        head = result_current_node
        moving_head = result_current_node
        val = 0
        carry = 0
        l1_current_node = l1
        l2_current_node = l2
        while l1_current_node.next != None and l2_current_node.next != None:
            val = l1_current_node.val + l2_current_node.val + carry
            if val >= 10:
                val = int(val%10)
                carry = 1
            else:
                val = val
                carry = 0
            prev_head = moving_head
            moving_head.val = val
            moving_head.next = ListNode()
            moving_head = moving_head.next
            l1_current_node = l1_current_node.next
            l2_current_node = l2_current_node.next
        if l1_current_node.next == None and l2_current_node.next == None:
            val = l1_current_node.val + l2_current_node.val + carry
            if val >= 10:
                val = int(val%10)
                carry = 1
                prev_head = moving_head
                moving_head.val = val
                moving_head.next = ListNode()
                moving_head = moving_head.next
                moving_head.val = carry
                moving_head.next = None
            else:
                val = val
                carry = 0
                prev_head = moving_head
                moving_head.val = val
                moving_head.next = None
        elif l1_current_node.next == None:
            val = l1_current_node.val + l2_current_node.val + carry
            if val >= 10:
                val = int(val%10)
                carry = 1
                prev_head = moving_head
                l1_current_node = l1_current_node.next
                l2_current_node = l2_current_node.next
                moving_head.val = val
                moving_head.next = l2_current_node
                while l2_current_node.next != None:
                    val = l2_current_node.val + carry
                    if val >= 10:
                        val = int(val%10)
                        carry = 1
                        l2_current_node.val = val
                        l2_current_node = l2_current_node.next
                    else:
                        carry = 0
                        l2_current_node = l2_current_node.next
                val = l2_current_node.val + carry
                if val >= 10:
                    val = int(val%10)
                    carry = 1
                    l2_current_node.val = val
                    l2_current_node.next = ListNode(val=1,next=None)
                else:
                    l2_current_node.val = val
                    
            else:
                val = val
                carry = 0
                l1_current_node = l1_current_node.next
                l2_current_node = l2_current_node.next
                prev_head = moving_head
                moving_head.val = val
                moving_head.next = l2_current_node
        else:
            val = l1_current_node.val + l2_current_node.val + carry
            if val >= 10:
                val = int(val%10)
                carry = 1
                prev_head = moving_head
                l1_current_node = l1_current_node.next
                l2_current_node = l2_current_node.next
                moving_head.val = val
                moving_head.next = l1_current_node
                while l1_current_node.next != None:
                    val = l1_current_node.val + carry
                    if val >= 10:
                        val = int(val%10)
                        carry = 1
                        l1_current_node.val = val
                        l1_current_node = l1_current_node.next
                    else:
                        carry = 0
                        l1_current_node = l1_current_node.next
                val = l1_current_node.val + carry
                if val >= 10:
                    val = int(val%10)
                    carry = 1
                    l1_current_node.val = val
                    l1_current_node.next = ListNode(val=1,next=None)
                else:
                    l1_current_node.val = val
            else:
                val = val
                carry = 0
                l1_current_node = l1_current_node.next
                l2_current_node = l2_current_node.next
                prev_head = moving_head
                moving_head.val = val
                moving_head.next = l1_current_node
        return result_current_node
