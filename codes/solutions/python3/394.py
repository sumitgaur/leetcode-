class Solution:
    def decodeString(self, s):
        stack, num, string = [], 0, ""
        for c in s:
            if c == "[":
                stack += string,
                stack += num,
                num, string = 0, ""
            elif c == "]":
                pre_num, pre_string = stack.pop(), stack.pop()
                string = pre_string + pre_num * string
            elif c.isdigit(): num = num * 10 + int(c)
            else: string += c
        return string

    class Solution:
        def decodeString(self, s: str) -> str:
            st = []
            i = 0
            for i in range(len(s)):
                if s[i] != "]":
                    st.append(s[i])
                else:
                    substr = ""
                    while st[-1] != "[":
                        substr = st.pop() + substr
                    st.pop()
                    k = ""
                    while st and st[-1].isdigit():
                        k = st.pop() + k
                    st.append(int(k) * substr)
            return ''.join(st)