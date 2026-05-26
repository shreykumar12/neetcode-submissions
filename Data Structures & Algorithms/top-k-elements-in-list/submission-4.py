class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = []
        freq = Counter(nums)


        for i in range(len(nums) + 1):
            buckets.append([])

        for key, value in freq.items():
            buckets[value].append(key)

        i = 0
        res = []

        for bucket in reversed(buckets):
            if bucket:
                for item in bucket:
                    res.append(item)
                    i += 1
                    if i == k:
                        return res
        return []

        

       

        