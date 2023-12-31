// https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        finallist = ListNode()
        finalcur = finallist
        finalprev = finalcur
        cur1 = list1
        cur2 = list2

        if cur1 == None and cur2 == None:
            finallist = None

        while cur1 != None and cur2 != None:
            if cur1.val < cur2.val:
                finalcur.val = cur1.val
                finalcur.next = ListNode()
                finalprev = finalcur
                finalcur = finalcur.next
                cur1 = cur1.next
            else:
                finalcur.val = cur2.val
                finalcur.next = ListNode()
                finalprev = finalcur
                finalcur = finalcur.next
                cur2 = cur2.next
        while cur1 != None:
            finalcur.val = cur1.val
            finalcur.next = ListNode()
            finalprev = finalcur
            finalcur = finalcur.next
            cur1 = cur1.next
        while cur2 != None:
            finalcur.val = cur2.val
            finalcur.next = ListNode()
            finalprev = finalcur
            finalcur = finalcur.next
            cur2 = cur2.next
        finalprev.next = None
        return finallist

            
        