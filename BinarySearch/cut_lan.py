# K: 랜선의 개수, N: 만들수 있는 랜선의 개수, lines: K개의 랜선
def solution(target, lines):
    answer = 0
    # lines 오름차순 정렬
    lines.sort() # O(NlogN)
    # [247,539,743,802]
    min_len, max_len = 1, max(lines)
    # 최소가 최대보다 같거나 작을때 까지만 루프
    while min_len <= max_len:
        mid_len = (min_len + max_len) // 2
        # 중간 랜선의 길이로 몇개를 만들수 있는지 판별
        total = sum(line // mid_len for line in lines)
        if total >= target: # 길이가 작아서 target보다 많거나 같기때문에 최대 길이를 구함
            answer = mid_len
            min_len += 1
        else: # 길이가 너무 커서 개수가 부족하므로
            max_len -= 1
    return answer

print(solution(11,[802,743,457,539]))