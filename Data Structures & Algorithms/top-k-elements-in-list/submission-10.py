class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        heap = []
        res = []

        for key in freqs.keys():
            heapq.heappush(heap, (-freqs[key], key))
        
        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        
        return res



                    


