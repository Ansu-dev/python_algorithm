from collections import deque




def solution(graph):
    year = 0
    row = len(graph)
    col = len(graph[0])

    # 얼음 부분을 담아둠
    ices = []
    for i in range(row):
        for j in range(col):
            if graph[i][j]:
                ices.append((i, j))

    def bfs(x, y):
        # 방향 탐색
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        q = deque([(x, y)])
        visited[x][y] = 1

        # 바다 리스트
        sea_list = []
        while q:
            x, y = q.popleft()
            sea = 0
            # 빙하 주변으로 바다가 있는지 탐색
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                # 그래프의 범위 설정
                if 0 <= nx < row and 0 <= ny < col:
                    # 바다를 만났다면 sea의 +1
                    if not graph[nx][ny]:
                        sea += 1
                    # 바다가 아니고 방문한적이 없다면 해당 빙하를 queue에 넣고 방문 처리
                    elif graph[nx][ny] and not visited[nx][ny]:
                        q.append((nx, ny))
                        visited[nx][ny] = 1
            # 빙하 주변에 바다가 있다면 해당 빙하 좌표와 바다의 개수를 배열에 쌓음
            if sea > 0:
                sea_list.append((x, y, sea))

        # sea_list에 저장한 빙산을 녹이기
        for x, y, sea in sea_list:
            graph[x][y] = max(0, graph[x][y] - sea) # 빙하에서 바다수만큼 빼줌 - 음수가 되는걸 방지하여 0보다 작으면 0을 넣음

        return 1


                # 얼음이 모두 사라질 때까지 루프
    while ices:
        # 빙산을 순회할 때 마다 방문 초기화
        visited = [[0] * col for _ in range(row)]
        # 삭제시 킬 리스트
        del_list = []
        group = 0
        for i, j in ices:
            if graph[i][j] and not visited[i][j]:
                group += bfs(i, j) # i, j를 기준으로 bfs를 수행

            # 원래 빙산이었던 부분에서 0으로 바뀐부분을 삭제 리스트에 넣음
            if graph[i][j] == 0:
                del_list.append((i, j)) # 빙하가 녹아 없어졌다면 삭제 시킬 리스트에 추가

        # 빙산이 2덩이가 넘으면 해당 answer을 retur
        if group > 1:
            return year

        # 기존 빙산 좌표에서 녹아 없어진 빙산 좌표를 제거
        ices = sorted(list(set(ices) - set(del_list)))
        year += 1


    # while이 끝나기 전에도 year를 반환하지 않았다면
    # 빙산이 모두 녹을때 까지 group을 2이상 만들지 못함
    return 0

print(solution(
        [
            [0,0,0,0,0,0,0],
            [0,2,4,5,3,0,0],
            [0,3,0,2,5,2,0],
            [0,7,6,2,4,0,0],
            [0,0,0,0,0,0,0]
        ]
    )
)