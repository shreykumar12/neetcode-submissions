class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        freq = {}
        res = []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for key, value in freq.items():
            buckets[value].append(key)
        
        i = 0
        for bucket in reversed(buckets):
            if bucket:
                for item in bucket:
                    res.append(item)
                    i += 1
                    if i == k:
                        return res
        return []

        
        