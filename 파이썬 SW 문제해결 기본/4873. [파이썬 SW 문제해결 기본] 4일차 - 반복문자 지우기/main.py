import sys

sys.stdin = open("./input.txt")

test_case_num = int(input())

for test_case_index in range(test_case_num):
    result = 0
    temp_str = input()
    stack = []
    for value in temp_str:
        if len(stack) == 0:
            stack.append(value)
            result += 1
        elif stack[-1] == value:
            stack.pop()
            result -= 1
        else:
            stack.append(value)
            result += 1
    print("#%d %d" % (test_case_index + 1, result))
