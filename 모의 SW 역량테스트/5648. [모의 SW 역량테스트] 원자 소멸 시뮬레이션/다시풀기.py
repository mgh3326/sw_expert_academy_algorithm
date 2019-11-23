import sys

sys.stdin = open("./data/sample_input (7).txt")

dir_list = [
    [1, 0],
    [-1, 0],
    [0, -1],
    [0, 1],
]
T = int(input())
for test_case_idx in range(T):
    result = 0
    N = int(input())
    atom_dict = {}
    for i in range(N):
        x, y, d, K = map(int, input().split())
        h, w = 2 * y, 2 * x
        atom_dict[i] = [h, w, d, K]
    while True:
        if len(atom_dict) == 0:
            break
        save_dict = {}
        for idx in list(atom_dict.keys()):
            h, w, d, K = atom_dict[idx]
            dh, dw = dir_list[d]
            nh, nw = h + dh, w + dw
            if nh > 2000 or nw > 2000 or nh < -2000 or nw < -2000:
                atom_dict.pop(idx)
                continue
            atom_dict[idx][0] = nh
            atom_dict[idx][1] = nw
            if (nh, nw) not in save_dict:
                save_dict[nh, nw] = [K, idx]
            else:
                atom_dict.pop(idx)
                result += K
                if save_dict[nh, nw][0] == 0:
                    pass
                else:
                    atom_dict.pop(save_dict[nh, nw][1])
                    result += save_dict[nh, nw][0]
                    save_dict[nh, nw][0] = 0

    print("#%d %d" % (test_case_idx + 1, result))
