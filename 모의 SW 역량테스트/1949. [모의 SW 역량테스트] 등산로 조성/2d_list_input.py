def add(a, b):
    return int(a) + int(b) + 1


def solution():
    test_case_num = int(input())
    for test_case_index in range(test_case_num):
        n, k = map(int, input().split())
        # 입력의 첫 번째 줄은 배열의 행 수입니다.
        map_arr = []
        for i in range(n):
            map_arr.append(list(map(int, input().split())))
        print("t")


solution()
