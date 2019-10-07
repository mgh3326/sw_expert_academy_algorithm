import sys

sys.stdin = open("./sample_input.txt")

test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = 0
    _, truck_list_len = map(int, input().split())
    container_list = list(map(int, input().split()))
    truck_list = list(map(int, input().split()))
    container_list.sort(reverse=True)
    truck_list.sort(reverse=True)
    truck_index = 0
    for container in container_list:
        if truck_index == truck_list_len:
            break
        if container <= truck_list[truck_index]:
            result += container
            truck_index += 1
    print("#%d %d" % (test_case_index + 1, result))
