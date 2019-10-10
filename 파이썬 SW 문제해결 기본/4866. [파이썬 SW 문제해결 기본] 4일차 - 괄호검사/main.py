import sys

sys.stdin = open("./input.txt")

test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = 0
    temp_str = input()
    stack = []
    for value in temp_str:
        if value == "(" or value == "{":
            stack.append(value)
        elif value == ")":
            if len(stack) == 0:
                break
            pop = stack.pop()
            if pop != "(":
                break
        elif value == "}":
            if len(stack) == 0:
                break
            pop = stack.pop()
            if pop != "{":
                break
    else:
        if len(stack) == 0:
            result = 1
    print("#%d %s" % (test_case_index + 1, result))
