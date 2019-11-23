dx = [1, 0, -1, 0]  # Right, down, left, up
dy = [0, 1, 0, -1]

# init
test_case_num = int(input())
for test_case_index in range(test_case_num):
    n, x = map(int, input().split())  # M : 총 이동시간, A : BC의 개수
    current_count = 0
    runway_list = []
    for _ in range(n):
        temp_list = list(map(int, input().split()))  # M : 총 이동시간, A : BC의 개수
        runway_list.append(temp_list)
    for i in range(n):
        temp_list = []
        for j in range(n):
            temp_list.append(runway_list[j][i])
        runway_list.append(temp_list)
    for runway in runway_list:
        max1 = max(runway)
        min1 = min(runway)
        if max1 == min1:  # 가능 ^^
            current_count += 1
            continue
        # (해결) 아래 조건을 창의적으로 할수 있을까? 예외처리를 해줌으로서 코드가 매우 지저분해졌다 [visit list 활용]
        else:  # 올라갈때만 중요하다 내려올때는 이전에 있던게 중요치 않다
            is_end = True
            is_down = False
            is_status = False
            saved_way = runway[0]
            temp_count = 1
            for way in runway[1:]:
                if abs(way - saved_way) > 1:  # 1보다 크면 지지대로 불가
                    is_end = False
                    break
                if saved_way > way:  # 하강
                    if is_down:
                        if temp_count >= x:
                            saved_way = way
                            temp_count = 1
                            is_down = True
                        else:
                            break
                    else:
                        saved_way = way
                        temp_count = 1
                        is_down = True
                elif saved_way == way:  # 같을때
                    saved_way = way
                    temp_count += 1
                else:  # 상승할때
                    if is_down == True:
                        temp_count -= x
                    if temp_count >= x:
                        saved_way = way
                        temp_count = 1
                        is_down = False
                    else:
                        is_end = False
                        break

            if is_end == True:  # 하강 중이었는지 확인 할 필요가 있네
                if is_down == True:
                    if temp_count >= x:
                        current_count += 1
                else:
                    current_count += 1

    print("#%d %d" % (test_case_index + 1, current_count))
