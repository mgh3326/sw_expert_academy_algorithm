import sys

sys.stdin = open("./data/sample_input.txt")

for tc in range(int(input())):
    T, B_num = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    battery_map = [[[(8, 0)], [(8, 0)], [(8, 0)], [(8, 0)], [(8, 0)], [(8, 0)], [(8, 0)], [(8, 0)], [(8, 0)], [(8, 0)]]
                   for i in range(10)]

    # 배터리정보
    for battery in range(B_num):
        X, Y, Range, Capacity = map(int, input().split())
        X, Y = X - 1, Y - 1

        # 충전범위
        for x in range(X - Range, X + Range + 1):
            gap = Range - abs(X - x)
            for y in range(Y - gap, Y + gap + 1):
                if 0 <= x <= 9 and 0 <= y <= 9:
                    battery_map[y][x] += [(battery, Capacity)]

    dx = [0, 0, 1, 0, -1]
    dy = [0, -1, 0, 1, 0]

    ax, ay = 0, 0
    bx, by = 9, 9
    my_max = 0

    for move in range(T + 1):  # T번의 이동

        order = sorted(battery_map[ay][ax], key=lambda x: x[1], reverse=True)
        order2 = sorted(battery_map[by][bx], key=lambda x: x[1], reverse=True)
        a_max = order[0]
        b_max = order2[0]

        if a_max[0] == b_max[0] and a_max[0] != 8:  # 둘의 현재 위치에서 최대 배터리가 같을 때,
            a_sem = order[1]
            b_sem = order2[1]

            if a_sem == b_sem == (8, 0):
                my_max += a_max[1]

            else:
                my_max += (a_max[1] + max(a_sem[1], b_sem[1]))

        else:  # 둘 중 하나만 충전이거나 충전할 거 없으면
            my_max += (a_max[1] + b_max[1])

        if move == T:
            break

        direction_a = A[move]
        ax, ay = ax + dx[direction_a], ay + dy[direction_a]
        direction_b = B[move]
        bx, by = bx + dx[direction_b], by + dy[direction_b]

    print('#{} {}'.format(tc + 1, my_max))
