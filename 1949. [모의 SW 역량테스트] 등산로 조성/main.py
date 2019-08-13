def add(a, b):
    return int(a) + int(b) + 1


def solution():
    test_case_num = int(input())
    for test_case_index in range(test_case_num):
        n, k = map(int, input().split())
        # 입력의 첫 번째 줄은 배열의 행 수입니다.
        map_list = []
        for i in range(n):
            map_list.extend(list(map(int, input().split())))
        max_num = max(map_list)
        max_num_index_list = [i for i, val in enumerate(map_list) if val == max_num]
        # 와 코드를 이렇게도 짤수 있구나 if 저게 True면 i를 반환하나보다 멋지다리
        

        print("t")


solution()
