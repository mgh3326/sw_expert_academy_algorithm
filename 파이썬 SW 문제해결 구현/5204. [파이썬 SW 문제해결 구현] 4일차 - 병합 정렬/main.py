import sys

sys.stdin = open("./input.txt")


# copy 메소드 때문에 runtime error가 났다. recursionlimit 때문일까?
def merge_sort(input_list):
    global result
    output_list = input_list
    if len(output_list) < 2:
        return output_list
    left_list = output_list[:len(output_list) // 2]
    right_list = output_list[len(output_list) // 2:]
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    # contour
    left_index = 0
    right_index = 0
    current_index = 0
    if len(left_list) == 0 or len(right_list) == 0:
        pass
    else:
        if left_list[-1] > right_list[-1]:
            result += 1
    while True:
        if left_index == len(left_list):
            while True:
                if right_index == len(right_list):
                    break
                output_list[current_index] = right_list[right_index]
                current_index += 1
                right_index += 1
            break
        if right_index == len(right_list):
            while True:
                if left_index == len(left_list):
                    break
                output_list[current_index] = left_list[left_index]
                current_index += 1
                left_index += 1
            break
        if left_list[left_index] < right_list[right_index]:
            output_list[current_index] = left_list[left_index]
            left_index += 1
        else:
            output_list[current_index] = right_list[right_index]
            right_index += 1
        current_index += 1

    return output_list


test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = 0
    n = int(input())

    my_list = list(map(int, input().split()))
    result_list = merge_sort(my_list)
    print("#%d %d %d" % (test_case_index + 1, result_list[n // 2], result))
