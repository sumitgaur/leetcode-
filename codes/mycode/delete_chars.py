def delete_chars_with_backspace(s):
    st = []
    for c in s:
        if c == '#':
            st and st.pop()
        else:
            st.append(c)
    return ''.join(st)


s1 = 'a##c'
print(delete_chars_with_backspace(s1))
