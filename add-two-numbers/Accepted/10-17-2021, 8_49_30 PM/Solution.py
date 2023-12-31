// https://leetcode.com/problems/add-two-numbers

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result_it = result_prev = result = ListNode()
        carry = 0
        while l1 or l2 or carry:
            if l1:
                result_it.val += l1.val
                l1 = l1.next
            if l2:
                result_it.val += l2.val
                l2 = l2.next

            result_it.next = ListNode(result_it.val // 10)
            result_it.val %= 10
            result_prev = result_it
            result_it = result_it.next
        if result_it.val == 0: result_prev.next = None
        return result