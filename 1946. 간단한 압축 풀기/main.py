import sys

sys.stdin = open("./data/input.txt")

T = int(input())
for test_case_idx in range(T):
    N = int(input())
    output_str = ""
    for i in range(N):
        C, K = map(str, input().split())
        K = int(K)
        output_str += C * K
    print("#%d" % (test_case_idx + 1))
    current_idx = 0
    while True:
        if current_idx >= len(output_str):
            break
        print(output_str[current_idx:current_idx + 10])
        current_idx += 10
