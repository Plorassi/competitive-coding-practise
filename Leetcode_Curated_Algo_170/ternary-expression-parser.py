class Solution:
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        i = len(expression)-1
        st = []
        while i >= 0:
            ch = expression[i]
            if ch.isdigit():
                st.append(ch)
                i -= 1
            elif ch in ("T", "F"):
                st.append(ch)
                i -= 1
            elif ch == ":":
                i -= 1
            elif ch == "?":
                i -= 1
                true = st.pop()
                false = st.pop()
                if expression[i] == "T":
                    st.append(true)
                else:
                    st.append(false)
                i -= 1
        return st[-1]
