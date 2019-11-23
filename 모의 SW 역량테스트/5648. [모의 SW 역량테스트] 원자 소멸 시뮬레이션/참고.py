T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    atoms = [list(map(int, input().split())) for _ in range(N)]
    for atom in atoms:
        atom[0] *= 2
        atom[1] *= 2
    energy = 0
    candidates = [[0, 0, 0]]
    for i in range(N - 1):
        for j in range(i, N):
            dx = atoms[i][0] - atoms[j][0]
            dy = atoms[i][1] - atoms[j][1]
            v1 = atoms[i][2]
            v2 = atoms[j][2]
            if dy == 0:
                if v1 == 2 and v2 == 3 and dx > 0:
                    candidates.append([dx // 2, i, j])
                elif v1 == 3 and v2 == 2 and dx < 0:
                    candidates.append([-dx // 2, i, j])
            elif dx == 0:
                if v1 == 0 and v2 == 1 and dy < 0:
                    candidates.append([-dy // 2, i, j])
                elif v1 == 1 and v2 == 0 and dy > 0:
                    candidates.append([dy // 2, i, j])
            elif dx == dy:
                if dx < 0 and v1 == 3 and v2 == 1:
                    candidates.append([-dx, i, j])
                elif dx < 0 and v1 == 0 and v2 == 2:
                    candidates.append([-dx, i, j])
                elif dx > 0 and v1 == 1 and v2 == 3:
                    candidates.append([dx, i, j])
                elif dx > 0 and v1 == 2 and v2 == 0:
                    candidates.append([dx, i, j])
            elif dx == -dy:
                if dx < 0 and v1 == 3 and v2 == 0:
                    candidates.append([-dx, i, j])
                elif dx < 0 and v1 == 1 and v2 == 2:
                    candidates.append([-dx, i, j])
                elif dx > 0 and v1 == 0 and v2 == 3:
                    candidates.append([dx, i, j])
                elif dx > 0 and v1 == 2 and v2 == 1:
                    candidates.append([dx, i, j])
    visited = [0] * N
    candidates.sort()
    collision = []
    for i in range(len(candidates) - 1):
        if candidates[i][0] != candidates[i + 1][0]:
            while collision:
                temp = collision.pop()
                if not visited[temp]:
                    visited[temp] = 1
                    energy += atoms[temp][3]

            if not visited[candidates[i + 1][1]] and not visited[candidates[i + 1][2]]:
                collision.append(candidates[i + 1][1])
                collision.append(candidates[i + 1][2])
        else:
            if not visited[candidates[i + 1][1]] and not visited[candidates[i + 1][2]]:
                collision.append(candidates[i + 1][1])
                collision.append(candidates[i + 1][2])
    while collision:
        temp = collision.pop()
        if not visited[temp]:
            visited[temp] = 1
            energy += atoms[temp][3]
    print('#{} {}'.format(tc, energy))
