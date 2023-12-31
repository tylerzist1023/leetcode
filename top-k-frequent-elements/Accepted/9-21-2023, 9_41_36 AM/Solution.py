// https://leetcode.com/problems/top-k-frequent-elements

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        numbers = {}
        for n in nums:
            if numbers.has_key(n):
                numbers[n] += 1
            else:
                numbers[n] = 1
        
        top_k_vals = []
        for i in range(k):
            maxn = 0
            for n in numbers:
                if not numbers.has_key(maxn) or numbers[n] > numbers[maxn]:
                    maxn = n
            top_k_vals.append(maxn)
            del numbers[maxn]

        return top_k_vals