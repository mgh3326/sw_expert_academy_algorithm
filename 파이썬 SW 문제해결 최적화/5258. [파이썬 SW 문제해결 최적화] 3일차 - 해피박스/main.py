import sys

sys.stdin = open("./input.txt")


def find_knapsack(p, w):
    if knapsack[p][w] != -1:
        return knapsack[p][w]
    current_price, current_weight = board_list[p - 1]
    # TODO knapsack 공부 추가적으로 필요하다
    # case1 -> n 번째 물건 포함
    # case1 -> n 번째 물건 미포함
    case1 = 0
    if current_weight <= w:
        case1 = find_knapsack(p - 1, w - current_weight) + current_price
    case2 = find_knapsack(p - 1, w)
    knapsack[p][w] = max(case1, case2)
    return knapsack[p][w]


test_case_num = int(input())
for test_case_index in range(test_case_num):
    total_weight, m = map(int, input().split())
    result = 0
    board_list = []
    knapsack = [[0] * (total_weight + 1)]
    for i in range(m):
        size, price = map(int, input().split())
        knapsack.append([-1] * (total_weight + 1))
        board_list.append([price, size])
    result = find_knapsack(m, total_weight)
    print("#%d %d" % (test_case_index + 1, result))
