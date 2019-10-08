import sys

sys.stdin = open("./input.txt")


def dfs(depth, start_index):
    global result
    global current_sum
    if depth == n:
        if current_sum == m:
            result += 1
        return
    for i in range(start_index, max_num + 1):
        current_sum += i
        if current_sum > m:
            current_sum -= i
            break
        dfs(depth + 1, i + 1)
        current_sum -= i


test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = 0
    current_sum = 0
    n, m = (map(int, input().split()))
    max_num = 12
    dfs(0, 1)
    print("#%d %d" % (test_case_index + 1, result))
