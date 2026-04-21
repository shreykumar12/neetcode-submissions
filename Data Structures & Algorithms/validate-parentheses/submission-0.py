class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        valid = {"[":"]", "{":"}", "(":")"}

        for c in s:
            if c in valid:
                st.append(c)
            else:
                if st and valid[st[-1]] == c:
                    st.pop()
                else:
                    return False
                    
        return not st