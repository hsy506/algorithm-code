# 로또의 최고 순위와 처저 순위
def solution(lottos, win_nums):
    answer = []
    # 배열 내림차순 정렬
    lottos.sort(reverse=True)
    win_nums.sort(reverse=True)

    # 0의 개수 세기
    zero_cnt = 0
    for i in range(0, 6):
        if lottos[i] == 0:
            zero_cnt += 1

    ans = 0
    for i in range(0, 6):
        for j in range(0, 6):
            if win_nums[i] == lottos[j]:
                ans += 1
                break
            else:
                if win_nums[i] > lottos[j]:
                    break
    # 맞은 번호가 없고, zero가 없는 경우 -> 최고 순위: 6, 최저 순위: 6
    if ans == 0 and zero_cnt == 0:
        answer = [6, 6]
    # 맞은 번호가 없고, zero가 있는 경우 -> 최고 순위: 6-zero_cnt+1, 최저 순위: 6
    elif ans == 0 and zero_cnt != 0:
        answer = [6-zero_cnt+1, 6]
    # 맞은 번호가 있고, zero가 없는 경우 -> 최고 순위: 6-ans+1, 최저 순위: 6-ans+1
    elif ans != 0 and zero_cnt == 0:
        answer = [6-ans+1, 6-ans+1]
    # 맞은 번호가 있고, zero가 있는 경우 -> 최고 순위: 6-(ans+zero_cnt)+1, 최저 순위: 6-ans+1
    else:
        answer = [6-(ans+zero_cnt)+1, 6-ans+1]
    return answer
