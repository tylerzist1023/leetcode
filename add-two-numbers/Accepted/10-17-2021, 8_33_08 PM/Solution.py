// https://leetcode.com/problems/add-two-numbers

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        result_it = result
        while True:
            # add the vals from each node if they exist
            if l1 != None:
                result_it.val += l1.val
                l1 = l1.next
            if l2 != None:
                result_it.val += l2.val
                l2 = l2.next

            # if the result is greater than 9, it means we have a carry, 
            #   so set carry to 1, and drop the 10s digit from result
            carry = 0
            if result_it.val > 9:
                carry = 1
                result_it.val %= 10

            if l1 == None and l2 == None and carry == 0:
                break 
            else:
                # init next to a new node. initialize it with the carry value (0 or 1 depending on the previous digit)
                result_it.next = ListNode(carry) 
                result_it = result_it.next

        return result