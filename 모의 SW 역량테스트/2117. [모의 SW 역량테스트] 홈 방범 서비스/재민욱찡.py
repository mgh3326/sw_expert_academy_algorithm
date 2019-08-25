def get_service_cost(K):
    return (K + 1) * (K + 1) + K * K


for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    maxCount = 0;
    maxK = 2 * N - 1
    for r in range(N):
        for c in range(N):
            counts = [0] * maxK
            for r1 in range(N):
                for c1 in range(N):
                    if grid[r1][c1] > 0:
                        counts[abs(r - r1) + abs(c - c1)] += 1
            countsSum = sum(counts)
            for k in range(maxK - 1, -1, -1):
                if countsSum * M >= get_service_cost(k):
                    maxCount = max(maxCount, countsSum)
                    break
                countsSum -= counts[k]
    print("#{} {}".format(test_case, maxCount))
