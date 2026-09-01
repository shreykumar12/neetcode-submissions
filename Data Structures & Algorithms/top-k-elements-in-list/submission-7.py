class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = []
        counts = Counter(nums)
        res = []

        for i in range(len(nums) + 1):
            buckets.append([])
        for key, value in counts.items():
            buckets[value].append(key)
        
        j = 0
        for bucket in reversed(buckets):
            if bucket:
                for n in bucket:
                    if len(res) < k:
                        res.append(n)
                if len(res) == k:
                    break
        
        return res