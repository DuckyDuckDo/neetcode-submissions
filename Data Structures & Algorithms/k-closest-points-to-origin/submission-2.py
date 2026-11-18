class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        def get_distance_to_origin(x, y):
            return (x**2 + y**2)**0.5

        for point in points:
            heapq.heappush(heap, (get_distance_to_origin(point[0], point[1]), point))
        
        res = []
        while heap and k > 0:
            res.append(heapq.heappop(heap)[-1])
            k -= 1
        
        return res