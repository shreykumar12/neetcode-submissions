class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        freq = {}
        res = []

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        for key, val in freq.items():
            buckets[val].append(key)
        
        for bucket in reversed(buckets):
            if bucket:
                for val in bucket:
                    if len(res) < k:
                        res.append(val)
                    else:
                        return res
        return res

        



        return[0]