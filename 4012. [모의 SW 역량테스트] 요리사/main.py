import sys

sys.stdin = open("./data/sample_input.txt")


def dfs(depth, start_idx):
    global result
    if depth == N // 2:
        temp_set = set(temp_list)
        difference_list = list(total_set.difference(temp_set))
        if tuple(difference_list) in visit_set:  # 백트래킹
            return
        visit_set.add(tuple(temp_list))
        temp_value = 0
        difference_value = 0
        for first in range(N // 2 - 1):
            for second in range(first + 1, len(temp_list)):
                temp_value += memo_list[temp_list[second]][temp_list[first]]
        for first in range(N // 2 - 1):
            for second in range(first + 1, len(temp_list)):
                difference_value += memo_list[difference_list[second]][difference_list[first]]
        result = min(result, abs(temp_value - difference_value))
        return
    for i in range(start_idx, N):
        temp_list.append(i)
        dfs(depth + 1, i + 1)
        temp_list.pop()


test_case_num = int(input())
for test_case_idx in range(test_case_num):
    N = int(input())
    total_set = set([i for i in range(N)])
    result = 20001
    board_list = [list(map(int, input().split())) for _ in range(N)]
    memo_list = [[0 for _ in range(N)] for _ in range(N)]
    for h in range(1, N):
        for w in range(h):
            memo_list[h][w] = board_list[h][w] + board_list[w][h]
    # visit set을 만들자
    visit_set = set()
    temp_list = []
    dfs(0, 0)

    print("#%d %d" % (test_case_idx + 1, result))
