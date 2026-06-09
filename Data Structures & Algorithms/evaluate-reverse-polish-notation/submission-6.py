class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for token in tokens:
            if token == "+":
                op2 = int(st.pop())
                op1 = int(st.pop())
                st.append(op1 + op2)
            elif token == "-":
                op2 = int(st.pop())
                op1 = int(st.pop())
                st.append(op1 - op2)
            elif token == "*":
                op2 = int(st.pop())
                op1 = int(st.pop())
                st.append(op1 * op2)
            elif token == "/":    
                op2 = int(st.pop())
                op1 = int(st.pop())
                st.append(int(op1 / op2))
            else:
                st.append(token)

        return int(st[-1])