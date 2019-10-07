import sys

sys.stdin = open("./input.txt")


# TODO 재귀로 짜면 재귀 오류가 나는 문제 같았다. in-place로 구성하였다.
def quick_sort(arr):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    return sort(0, len(arr) - 1)


test_case_num = int(input())
for test_case_index in range(test_case_num):
    n = int(input())
    my_list = list(map(int, input().split()))
    quick_sort(my_list)
    print("#%d %d" % (test_case_index + 1, my_list[n // 2]))
