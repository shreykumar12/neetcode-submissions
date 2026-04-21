class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        ops = set(['+', '-', '/', '*'])

        for token in tokens:
            if token in ops:
                op2 = int(st.pop())
                op1 = int(st.pop())
                if token == '+':
                    sum = op1 + op2
                    st.append(sum)
                elif token == '-':
                    diff = op1 - op2
                    st.append(diff)
                elif token == '/':
                    ans = op1 / op2
                    st.append(ans)
                else:
                    prod = op1 * op2
                    st.append(prod)
            else:
                st.append(token)
        
        return int(st[-1])