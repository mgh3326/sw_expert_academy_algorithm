import sys

sys.stdin = open("./input.txt")

test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = -1
    n, m, l = map(int, input().split())
    my_list = list(map(int, input().split()))
    for _ in range(m):
        temp_list = input().split()
        if temp_list[0] == "I":
            index, num = map(int, temp_list[1:])
            my_list.insert(index, num)
        elif temp_list[0] == "D":
            index = int(temp_list[1])
            my_list.pop(index)

        elif temp_list[0] == "C":
            index, num = map(int, temp_list[1:])
            my_list[index] = num
    if l < len(my_list):
        result = my_list[l]
    print("#%d %s" % (test_case_index + 1, result))
