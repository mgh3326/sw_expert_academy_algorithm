import sys

sys.stdin = open("./input.txt")

test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = 0
    find_str = input()
    total_str = input()
    while True:
        find = total_str.find(find_str)
        if find == -1:
            break
        result += 1
        total_str = total_str[find + len(find_str):]
    print("#%d %s" % (test_case_index + 1, result))
