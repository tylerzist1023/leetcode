// https://leetcode.com/problems/linked-list-cycle

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from fractions import gcd

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        tortoise = head
        tortoise_i = 0
        hare = head
        hare_i = 0

        while tortoise or hare:
            tortoise = tortoise.next
            tortoise_i += 1
            if hare and hare.next:
                hare = hare.next.next
                hare_i += 2
            else:
                return False

            if hare == tortoise:
                return True

        
