// https://leetcode.com/problems/add-two-numbers

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # first, convert both lists to arrays
        l1arr = []
        l2arr = []
        while not (l1 == None and l2 == None):
            if l1 != None:
                l1arr.append(l1.val)
                l1 = l1.next
            if l2 != None:
                l2arr.append(l2.val)
                l2 = l2.next

        # then, convert the arrays to ints
        l1int = 0
        l2int = 0
        for i in range(len(l1arr)):
            l1int += l1arr[i]*(10**i)
        for i in range(len(l2arr)):
            l2int += l2arr[i]*(10**i)

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