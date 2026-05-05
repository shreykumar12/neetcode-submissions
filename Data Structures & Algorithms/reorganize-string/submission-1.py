class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = []
        for char, cnt in count.items():
            maxHeap.append([-cnt, char])
        #Make it a heap    
        heapq.heapify(maxHeap)

        prev = None
        res = ""
        while maxHeap or prev:
            if not maxHeap and prev: #Can't add cahr w/o causing duplicate
                return ""
            
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, char]
            
        return res
