class Solution:
    def maximumSwap(self, num):
        res, num = num, list(str(num))
        for i in range(len(num) - 1):
            for j in range(i + 1, len(num)):
                if int(num[j]) > int(num[i]):
                    tmp = int("".join(num[:i] + [num[j]] + num[i + 1:j] + [num[i]] + num[j + 1:]))
                    if tmp > res: res = tmp
        return res

    def maximumSwap1(self, num: int) -> int:
        def cmp(x, y):
            return int(str(x) + str(y)) > int(str(y) + str(x))

        return str(num)


def rotationalCipher(input_str, rotation_factor):
    # Write your code here
    input_str = list(input_str)

    for i in range(len(input_str)):
        if input_str[i].isalpha():
            gap = ord('a') - ord('z') - 1 if input_str[i].islower() else ord('A') - ord('Z') - 1
            new_ord = ord(input_str[i]) + (rotation_factor % 26)
            if new_ord > (ord('z') if input_str[i].islower() else ord('Z')):
                input_str[i] = chr(new_ord + gap)
            else:
                input_str[i] = chr(new_ord)
        if input_str[i].isdigit():
            new_ord = ord(input_str[i]) + rotation_factor % 10
            if new_ord > ord('9'):
                input_str[i] = chr(new_ord - ord('9') + ord('0') - 1)
            else:
                input_str[i] = chr(new_ord)
    return ''.join(input_str)


input = "All-convoYs-9-be:Alert1."
rotationFactor = 4
rotationalCipher(input, rotationFactor)
