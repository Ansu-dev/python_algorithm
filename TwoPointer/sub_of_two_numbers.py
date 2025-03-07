
# n: 수열의 길이, x: target 숫자, sequences: n길이의 수열
def solution(target, sequence):
    answer = 0
    # 두수의 합이 target을 만족하는 쌍이 몇개가 있는지
    left,right = 0, len(sequence) - 1
    sequence.sort()
    print(sequence)
    while left < right:
        sum_number = sequence[left] + sequence[right]
        if sum_number == target:
            answer += 1
            right -= 1
        elif sum_number < target:
            left += 1
        else:
            right -= 1
    return answer

print(solution(13, [5,12,7,10,9,1,2,3,11]))