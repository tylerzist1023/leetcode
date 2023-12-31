// https://leetcode.com/problems/add-two-numbers

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result_it = result = ListNode(0,ListNode())
        while l1 or l2 or carry:
            result_it = result_it.next

            # add the vals from each node if they exist
            if l1:
                result_it.val += l1.val
                l1 = l1.next
            if l2:
                result_it.val += l2.val
                l2 = l2.next

            # if the result is greater than 9, it means we have a carry, 
            #   so carry will be 1 if this is the case. 
            #   we can check this through integer division
            carry = result_it.val // 10
            result_it.val %= 10

            # init next to a new node. initialize it with the carry value (0 or 1 depending on the previous digit)
            result_it.next = ListNode(carry)
        result_it.next = None
        return result.next