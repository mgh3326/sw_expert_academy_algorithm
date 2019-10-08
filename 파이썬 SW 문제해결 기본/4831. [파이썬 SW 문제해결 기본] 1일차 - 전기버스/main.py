import sys

sys.stdin = open("./input.txt")

test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = 0
    k, n, m = map(int, input().split())
    charge_list = list(map(int, input().split()))
    charge_index = 0
    current_energy = k
    current_charge = 0
    for i in range(n):
        if charge_index != len(charge_list) and i == charge_list[charge_index]:
            current_charge = k
            charge_index += 1
        if current_energy == 0:
            current_energy = current_charge
            result += 1
        current_energy -= 1
        current_charge -= 1
        if current_energy < 0:
            result = 0
            break
    print("#%d %d" % (test_case_index + 1, result))
