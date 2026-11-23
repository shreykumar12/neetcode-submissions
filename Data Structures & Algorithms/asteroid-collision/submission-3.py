class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        st.append(asteroids[0])

        for a in asteroids[1:]:
            destroyed = False
            while st and st[-1] > 0 and a < 0:
                prevA = st[-1]
                if abs(a) == abs(prevA):
                    st.pop()
                    destroyed = True
                    break
                # different size 
                elif abs(prevA) < abs(a):
                    st.pop()
                else:
                    destroyed = True
                    break
            if not destroyed:
                st.append(a)
        return st

                
