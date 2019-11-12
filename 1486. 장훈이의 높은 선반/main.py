import sys

sys.stdin = open("./data/input.txt")


def dfs(depth):
    global current_h
    global result
    if current_h - B >= result:
        return
    if depth == N:
        if current_h >= B:
            result = min(result, current_h - B)
            return
        return
    dfs(depth + 1)
    current_h += S[depth]
    dfs(depth + 1)
    current_h -= S[depth]


T = int(input())
for test_case_idx in range(T):
    result = 10 ** 8
    N, B = map(int, input().split())
    S = list(map(int, input().split()))
    current_h = 0
    visit_set = set()
    temp_list = []
    dfs(0)
    print("#%d %d" % (test_case_idx + 1, result))
