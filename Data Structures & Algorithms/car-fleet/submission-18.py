class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st = []
        pairs = [[p, s] for p, s in zip(position, speed)]
        pairs.sort(key = lambda pair:pair[0], reverse=True)

        for i in range(len(position)):
            time = (target - pairs[i][0]) / pairs[i][1]
            if not st or time > st[-1]:
                st.append(time)
        
        return len(st)
