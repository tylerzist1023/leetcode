// https://leetcode.com/problems/add-two-numbers

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # first, convert both lists to ints
        l1int = 0
        l2int = 0
        i = 0
        while not (l1 == None and l2 == None):
            if l1 != None:
                l1int += l1.val*(10**i)
                l1 = l1.next
            if l2 != None:
                l2int += l2.val*(10**i)
                l2 = l2.next
            i += 1

        # get result, then convert back to linked list
        resultint = l1int + l2int
        result = ListNode()
        resultit = result
        while True:
            resultit.val = resultint % 10

            resultint //= 10
            if resultint > 0:
                resultit.next = ListNode()
                resultit = resultit.next
            else: break

        return result