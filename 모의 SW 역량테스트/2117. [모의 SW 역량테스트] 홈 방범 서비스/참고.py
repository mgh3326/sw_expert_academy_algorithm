# TODO DP로도 접근해보자
def main():
    testcases = int(input())
    for tc in range(1, testcases + 1):
        n, m = input_as_list()
        grid = [input_as_list() for _ in range(n)]
        houses = []

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    houses.append((i, j))

        out = 0
        for i in range(n):
            for j in range(n):
                by_dist = [0] * (2 * n)
                for x, y in houses:
                    by_dist[abs(i - x) + abs(j - y)] += 1
                for d in range(2 * n):
                    if d > 0:
                        by_dist[d] += by_dist[d - 1]
                    h = by_dist[d]
                    if m * h >= d * d + (d + 1) * (d + 1):
                        out = max(out, h)

        print(f"#{tc} {out}")


def input_as_list():
    return list(map(int, input().split()))


main()
