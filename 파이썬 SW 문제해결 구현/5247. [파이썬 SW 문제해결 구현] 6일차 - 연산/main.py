import sys

sys.stdin = open("./input.txt")

dir_list = [1, -1, -10]
test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = 0
    n, m = map(int, input().split())
    visit_list = [False] * 1000001
    visit_list[n] = True
    queue = []
    queue.append([n, 0])
    current_index = 0
    is_end = False
    # TODO BFS에서 메모리가 충분하다면 pop을 쓰지 않는 것도 좋은 방도이다.
    while True:
        pop, depth = queue[current_index]
        for _dir in dir_list:
            next_value = pop + _dir
            if next_value == m:
                is_end = True
                break
            if next_value < 0 or next_value > 1000000:
                continue
            if not visit_list[next_value]:
                queue.append([next_value, depth + 1])
                visit_list[next_value] = True
        if is_end:
            break
        next_value = pop * 2
        if next_value == m:
            break
        if next_value < 0 or next_value > 1000000:
            pass
        else:
            if not visit_list[next_value]:
                queue.append([next_value, depth + 1])
                visit_list[next_value] = True
        current_index += 1
    print("#%d %d" % (test_case_index + 1, depth + 1))
