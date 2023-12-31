// https://leetcode.com/problems/k-closest-points-to-origin

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for x,y in points:
            dist = sqrt((x**2) + (y**2))
            minheap.append([dist, x,y])

        heapq.heapify(minheap)

        res=[]
        while k > 0:
            k -= 1
            dist,x,y = heapq.heappop(minheap)
            res.append([x,y])
        
        return res