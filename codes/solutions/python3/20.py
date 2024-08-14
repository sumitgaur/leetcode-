class Solution:
    def isValid(self, s):
        brackets_stack, lefts, rights = [], ("(", "[", "{"), (")", "]", "}")
        for char in s:
            if char in lefts:
                brackets_stack.append(char)
            elif not brackets_stack or lefts.index(brackets_stack.pop()) != rights.index(char):
                return False
        return not brackets_stack

    def isValid_2(self, s: str) -> bool:
        st, pairs = [], {'(': ')', '{': '}', '[': ']'}
        for c in s:
            if c in pairs:
                st.append(c)
            elif not st or pairs[st.pop()] != c:
                return False
        return st == []
