import sys

sys.stdin = open("./input.txt")
test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = 0
    n, m = map(int, input().split())
    my_dict = {}
    visit_set = set()
    board_list = list(map(int, input().split()))
    for i in range(m):
        if board_list[i * 2] not in my_dict:
            my_dict[board_list[i * 2]] = []
        my_dict[board_list[i * 2]].append(board_list[i * 2 + 1])
        if board_list[i * 2 + 1] not in my_dict:
            my_dict[board_list[i * 2 + 1]] = []
        my_dict[board_list[i * 2 + 1]].append(board_list[i * 2])
    for i in range(n):
        current_index = i + 1
        if current_index not in visit_set:
            result += 1
            visit_set.add(current_index)
        else:
            continue
        queue = []
        queue.append(current_index)
        while True:
            if len(queue) == 0:
                break
            pop = queue.pop(0)
            if pop in my_dict:
                pop_ = my_dict[pop]
                for pop_value in pop_:
                    if pop_value not in visit_set:
                        queue.append(pop_value)
                        visit_set.add(pop_value)
    print("#%d %d" % (test_case_index + 1, result))
