// https://leetcode.com/problems/kth-largest-element-in-an-array

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = [-s for s in nums]
        heapq.heapify(maxheap)

        while k > 1:
            k -= 1
            heapq.heappop(maxheap)

        return heapq.heappop(maxheap)*-1