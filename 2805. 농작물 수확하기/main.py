import sys

sys.stdin = open("./data/input.txt")

T = int(input())
for test_case_idx in range(T):
    N = int(input())
    result = 0
    board_list = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        temp = input()
        for idx, value in enumerate(temp):
            board_list[i][idx] = int(value)
    for i in range(N // 2 + 1):
        result += board_list[i][N // 2]
        for j in range(i):
            result += board_list[i][N // 2 + j + 1] + board_list[i][N // 2 - j - 1]
    for i in range(N // 2):
        result += board_list[N // 2 + i + 1][N // 2]
        for j in range(N // 2 - i - 1):
            result += board_list[N // 2 + i + 1][N // 2 + j + 1] + board_list[N // 2 + i + 1][N // 2 - j - 1]
    print("#%d %d" % (test_case_idx + 1, result))
