class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = []

        for i in range(len(temperatures)):
            while st and temperatures[st[-1]] < temperatures[i]:
                index = st.pop()
                res[index] = i - index
            st.append(i)
        
        return res
