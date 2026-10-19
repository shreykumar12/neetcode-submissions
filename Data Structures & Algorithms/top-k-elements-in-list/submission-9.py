class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = []
        for i in range(len(nums) + 1):
            buckets.append([])
        res = []
        freq = Counter(nums)

        for key, val in freq.items():
            buckets[val].append(key)
        
        for bucket in reversed(buckets):
            if bucket:
                for n in bucket:
                    if len(res) < k:
                        res.append(n)
                    if len(res) == k:
                        break
        
        return res
                    


