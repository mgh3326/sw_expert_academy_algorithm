import sys

sys.stdin = open("./data/input1.txt", encoding='utf-8')

dh = [0, 1, 0, -1]  # 우 하 좌 상
dw = [1, 0, -1, 0]  # 우 하 좌 상
n, w = map(int, input().split())
my_list = []
result_list = []
for i in range(n):
    temp_list = input().split()
    my_list.append(temp_list)
    result_list.append([""] * n)
size = n
start_h = 0
start_w = 0
while True:
    if size < 1:
        break
    temp_list = []
    for i in range(len(dh)):
        for j in range(size-1):
            start_h += dh[i]
            start_w += dw[i]
            temp_list.append([start_h, start_w])
    if size == 1:
        result_list[start_h][start_w] = my_list[start_h][start_w]
    else:
        size_ = w % (size * 4 - 4)
        for i in range((size * 4 - 4)):
            result_list[temp_list[(i + size_) % len(temp_list)][0]][temp_list[(i + size_) % len(temp_list)][1]] = \
                my_list[temp_list[i][0]][temp_list[i][1]]
    size = size - 2
    start_h += 1
    start_w += 1
    w *= -1
for result in result_list:
    print(" ".join(result))
