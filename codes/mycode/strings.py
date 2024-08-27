import bisect
import re
from collections import OrderedDict

memo = {}


def rename_file(new_name, old_name):
    if new_name == old_name or new_name == "":
        return 1
    if old_name == "" or len(new_name) > len(old_name):
        return 0

    if (new_name, old_name) in memo:
        return memo[(new_name, old_name)]
    if new_name[0] == old_name[0]:
        memo[(new_name, old_name)] = do(new_name[1:], old_name[1:]) + do(new_name, old_name[1:])
    else:
        memo[(new_name, old_name)] = do(new_name, old_name[1:])
    return memo[(new_name, old_name)]


def replace_non_repeat(s):
    s = list(s)
    non_repeating = [s[0]]
    seen = set(s[0])
    res = [s[0]]
    for i in range(1, len(s)):
        if non_repeating:
            if non_repeating[0] != s[i]:
                res.append(non_repeating[0])
            else:
                non_repeating.pop(0)
                res.append(non_repeating[0] if non_repeating else "#")
        else:
            res.append(s[i])
        if s[i] not in seen:
            non_repeating.append(s[i])
            seen.add(s[i])
        elif s[i] in non_repeating:
            non_repeating.remove(s[i])

    return "".join(res)


def noPrefix(words):
    root = {}
    for word in words:
        cur = root
        for c in word:
            cur[c] = cur.get(c, {})
            if "END" in cur:
                print("BAD SET\n" + word)
                return
            cur = cur[c]
        cur["END"] = True
    print("GOOD SET")


# noPrefix(["abcd", "bcd", "abcde", "bcde"])


# Question:
# Given a sorted string arr = {"boo", "go","google","hello", "uxys"} and a prefix string = "go".
# return number of Strings that match with prefix.

def count_strings_with_prefix(arr, prefix):
    left = bisect.bisect_left(arr, prefix)
    right = bisect.bisect_right(arr, prefix + '~')
    return right - left


# arr = ["boo", "go", "google", "hello", "uxys"]
# prefix = "go"
# print(count_strings_with_prefix(arr, prefix))


#
# Given variable values such as x = "new"
# y= "%xworld"
# z="hello"
# example resolveString("z_%x_%y_world")


class FstringResolver:
    def __init__(self):
        self.vars_map = {'x': 'new', 'y': '%xworld', 'z': 'hello'}

    def resolve_string(self, f_string):
        if '%' not in f_string:
            return f_string
        while '%' in f_string:
            i = f_string.index('%')
            f_string = f_string.replace(f_string[i:i + 2],
                                        self.resolve_string(self.vars_map[f_string[i + 1]]))
        return f_string

    def update_string(self, x, v):
        self.vars_map[x] = v


# print(FstringResolver().resolve_string("%z_%x_%y_world"))

# I am doing well today,
# and I feel it's going
# to rain at 6PM. There
# hasn't been rain for quite significant time. The place has become very hot.
def word_wrap(sentence, width):
    lines = []
    for i in range(0, len(sentence), width):
        lines.append(sentence[i:i + width])
    return lines


# sentence = '''I am doing well today, and I feel it's going to rain at 6PM. There hasn't been rain for quite significant time. The place has become very hot.'''
# print(word_wrap(sentence, 15))

def sentence_break(sentence, width):
    words = sentence.split()
    lines = []
    current_line = ''
    for word in words:
        if len(word) + len(current_line) + 1 <= width:
            if current_line:
                current_line += ' '
            current_line += word + ' '
        else:
            lines.append(current_line)
            current_line = word + ' '
    return lines


def find_lines(sentence, width):
    """
    Assumption:
    longest word length is smaller than the width of the page
    """
    words = sentence.split()
    cur_line_length = 0
    lines = 0
    for word in words:
        if cur_line_length + len(word) + 1 <= width:
            cur_line_length += len(word) + 1
        else:
            lines += 1
            cur_line_length = len(word) + 1
    return lines


def fit_in_two_col_page(sentence1, sentence2, width):
    low = 0
    high = width
    lines_diff_so_far = 2 ** 32
    max_lines_needed = 0
    while low <= high:
        mid = (low + high) // 2
        req_lines1 = find_lines(sentence1, mid)
        req_lines2 = find_lines(sentence2, mid)
        if abs(req_lines1 - req_lines2) < lines_diff_so_far:
            lines_diff_so_far = abs(req_lines1 - req_lines2)
            max_lines_needed = max(req_lines1, req_lines2)
        if req_lines1 > req_lines2:
            low = mid + 1
        else:
            high = mid - 1
    return max_lines_needed


# Example usage


sentence = "This is an example sentence that we want to fit on a page minimizing word breaks."
sentences = ["leet code community discuss forum", "data structure and algorithm questions and patterns"]
page_width = 10
number_of_lines = fit_in_two_col_page(sentences[0], sentences[1], page_width)
print(f"Number of lines needed: {number_of_lines}")
