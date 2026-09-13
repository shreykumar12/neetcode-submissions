class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st = []
        sorts = [[p, s] for p, s in zip(position, speed)]
        time = 0
        sorts.sort(key=lambda sort: sort[0], reverse=True)

        for i in range(len(position)):
            time = ((target - sorts[i][0]) / sorts[i][1]) #time to destination
            if not st or time > st[-1]:
                st.append(time)
        
        return len(st)

