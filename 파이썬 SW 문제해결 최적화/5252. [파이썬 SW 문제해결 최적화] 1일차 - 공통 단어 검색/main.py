import sys

sys.stdin = open("./input.txt")

test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = 0
    n, m = map(int, input().split())
    save_set = set()
    for i in range(n):
        save_set.add(input())
    for i in range(m):
        temp_value = input()
        if temp_value in save_set:
            result += 1
    print("#%d %d" % (test_case_index + 1, result))
