# N: 수열의 길이, S: 수열의 합
# sequence: N길의 수열

# 10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N (10 ≤ N < 100,000)과 S (0 < S ≤ 100,000,000)가 주어진다. 둘째 줄에는 수열이 주어진다. 수열의 각 원소는 공백으로 구분되어져 있으며, 10,000이하의 자연수이다.

def solution(target, sequence):
    answer = len(sequence) + 1
    left,right = 0, 0 # 투 포인터를 배열의 시작점에 위치
    current_sum = 0 # 현재 윈도우의 합을 저장

    while True:
        if current_sum >= target:
            # 현재 저장된 길이와 target이 넘는 부분합의 길이중 더 짧은것을 저장
            answer = min(answer, right - left) # right는 범위에 포함되지 않으므로 +1을 안더하는게 맞다

            # 더 짧은 길이를 구하기 위해 left를 확장
            current_sum -= sequence[left]
            left += 1
        elif right == len(sequence): # right가 배열의 끝인덱스를 벗어났을 때
            break
        else:
            # 윈도우를 확장하기 위해 right 포인터 이동
            current_sum += sequence[right]
            right += 1
    return answer

print(solution(15, [5,1,3,5,10,7,4,9,2,8]))