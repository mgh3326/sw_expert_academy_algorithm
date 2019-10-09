import sys

sys.stdin = open("./input.txt")
# 문제를 잘 읽도록 하자
test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = 0
    charge_list = list(map(int, input().split()))
    n = charge_list.pop(0)
    current_list = []
    current_energy = charge_list[0]
    current_index = 1
    current_energy -= 1
    while True:

        if current_index == n - 1:
            break
        remove_list = []
        for i in range(len(current_list)):
            current_list[i] -= 1
            if current_list[i] == 0:
                remove_list.append(i)
        while True:
            if len(remove_list) == 0:
                break
            list_pop = remove_list.pop()
            current_list.pop(list_pop)
        current_list.append(charge_list[current_index])
        if current_energy == 0:
            current_list.sort()
            pop = current_list.pop()
            current_energy = pop
            result += 1
        current_energy -= 1
        current_index += 1
    print("#%d %d" % (test_case_index + 1, result))
