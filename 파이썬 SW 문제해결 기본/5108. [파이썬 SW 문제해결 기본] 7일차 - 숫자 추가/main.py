import sys

sys.stdin = open("./input.txt")

test_case_num = int(input())

for test_case_index in range(test_case_num):
    is_end = False
    result = 0
    n, m, l = map(int, input().split())
    my_list = list(map(int, input().split()))
    for i in range(m):
        index, num = map(int, input().split())
        my_list.insert(index, num)
    result = my_list[l]
    print("#%d %s" % (test_case_index + 1, result))
