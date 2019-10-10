import sys

sys.stdin = open("./input.txt")


def dfs(index):
    global is_end
    if index == end:
        is_end = True
        return
    for graph_index in graph[index]:
        if visit[index][graph_index]:
            continue
        visit[index][graph_index] = True
        dfs(graph_index)
        if is_end:
            return
        visit[index][graph_index] = False


test_case_num = int(input())

for test_case_index in range(test_case_num):
    is_end = False
    result = 0
    v, e = map(int, input().split())
    graph = []
    visit = []
    for i in range(v + 1):
        temp_list = [False] * (v + 1)
        visit.append(temp_list)
        graph.append(list())
    for i in range(e):
        start, end = map(int, input().split())
        graph[start].append(end)
    start, end = map(int, input().split())
    dfs(start)
    if is_end:
        result = 1
    print("#%d %s" % (test_case_index + 1, result))
