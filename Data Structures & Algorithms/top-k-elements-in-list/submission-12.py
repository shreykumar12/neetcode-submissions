class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = []
        freq = Counter(nums)
        res = []

        for i in range(len(nums) + 1):
            buckets.append([])

        for key, val in freq.items():
            buckets[val].append(key)
        
        for bucket in reversed(buckets):
            if bucket:
                for val in bucket:
                    if len(res) < k:
                        res.append(val)
                    if len(res) == k:
                        return res
        
        return res
        
        
