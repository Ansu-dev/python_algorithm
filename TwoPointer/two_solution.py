def solution(features):
    left, right = 0, len(features) - 1
    features.sort() # O(NlogN)
    min_abs_sum = float('inf')

    answer = (features[left], features[right])
    while left < right:
        current_sum = features[left] + features[right]
        # 현재의 합산을 절대값 최소보다 작은지 판별
        if abs(current_sum) < min_abs_sum:
            min_abs_sum = current_sum
            answer = (features[left],features[right])

        # 현재의 합산이 0인지 더 작은지 큰지를 판별
        if current_sum == 0:
            break
        elif current_sum < 0:
            left += 1
        else:
            right -= 1
    return answer

print(solution([-2,4,-99,-1,98]))