import sys

sys.stdin = open("./input.txt")

test_case_num = int(input())

for test_case_index in range(test_case_num):
    is_end = False
    result = 0
    v, e = map(int, input().split())
    graph = []
    visit = [False] * (v + 1)
    for i in range(v + 1):
        graph.append(list())
    for i in range(e):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)
    start, end = map(int, input().split())
    visit[start] = True
    queue = []
    queue.append([start, 0])
    queue_idx = 0
    while True:
        if queue_idx >= len(queue):
            break
        current_start, depth = queue[queue_idx]
        for current_end in graph[current_start]:
            if current_end == end:
                is_end = True
                result = depth + 1
                break
            if not visit[current_end]:
                visit[current_end] = True
                queue.append([current_end, depth + 1])
        if is_end:
            break
        queue_idx += 1

    print("#%d %s" % (test_case_index + 1, result))
