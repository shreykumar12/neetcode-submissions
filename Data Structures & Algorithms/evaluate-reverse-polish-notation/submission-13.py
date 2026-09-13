class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for t in tokens:
            if t == '+':
                op2 = int(st.pop())
                op1 = int(st.pop())
                st.append(op1 + op2)
            elif t == '-':
                op2 = int(st.pop())
                op1 = int(st.pop())
                st.append(op1 - op2)
            elif t == '*':
                op2 = int(st.pop())
                op1 = int(st.pop())
                st.append(op1 * op2)
            elif t == '/':
                op2 = int(st.pop())
                op1 = int(st.pop())
                st.append(int(op1 / op2))
            else:
                st.append(t)
        
        return int(st[-1])
            