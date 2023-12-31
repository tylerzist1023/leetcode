// https://leetcode.com/problems/add-two-numbers

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        result_it = result
        while True:
            carry = 0
            if l1 != None:
                result_it.val += l1.val
                l1 = l1.next
            if l2 != None:
                result_it.val += l2.val
                l2 = l2.next

            if result_it.val > 9:
                carry = 1
                result_it.val %= 10

            if l1 == None and l2 == None and carry == 0: # nothing more to add
                break
            else:
                result_it.next = ListNode(carry)
                result_it = result_it.next

        return result