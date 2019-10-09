import sys

sys.stdin = open("./input.txt")


def find_factorial(input_n):
    if factorial[input_n] != -1:
        return factorial[input_n]
    factorial[input_n] = input_n * find_factorial(input_n - 1)
    return factorial[input_n]


test_case_num = int(input())
for test_case_index in range(test_case_num):
    factorial = [-1] * 71
    factorial[0] = 1
    factorial[1] = 1
    factorial[2] = 2
    factorial[3] = 6
    n, a, b = map(int, input().split())
    # n C min1 을 구하면 된다
    result = find_factorial(n) // (find_factorial(a) * find_factorial(b))

    print("#%d %d" % (test_case_index + 1, result))
