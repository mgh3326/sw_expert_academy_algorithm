import sys

sys.stdin = open("./data/input.txt")
prime_number_list = [2, 3, 5, 7, 11]
T = int(input())
for test_case_idx in range(T):
    N = int(input())
    result_list = []
    for prime_number in prime_number_list:
        current_number = N
        count = 0
        while True:
            if current_number % prime_number != 0:
                break
            current_number //= prime_number
            count += 1
        result_list.append(str(count))
    result = " ".join(result_list)
    print("#%d %s" % (test_case_idx + 1, result))
