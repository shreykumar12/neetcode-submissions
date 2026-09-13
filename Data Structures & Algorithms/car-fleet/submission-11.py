class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st = []
        sorts = []
        time = 0
        for i in range(len(position)):
            sorts.append([position[i], speed[i]])
        sorts.sort(key=lambda sort: sort[0], reverse=True)
        #print(sorts)
        for i in range(len(position)):
            time = ((target - sorts[i][0]) / sorts[i][1]) #time to destination
            if not st or time > st[-1]:
                st.append(time)
        
        return len(st)

