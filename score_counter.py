def count_chinese_score(board):
    size = len(board)

    def is_within_bounds(row, col):
        """Проверка, что координаты находятся в пределах доски"""
        return 0 <= row < size and 0 <= col < size

    def get_group(row, col):
        """Получение группы связанных камней|пустых полей"""
        _color = board[row][col]
        group = set()
        stack = [(row, col)]
        while stack:
            r, c = stack.pop()
            if (r, c) in group:
                continue
            group.add((r, c))
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if is_within_bounds(nr, nc) and board[nr][nc] == _color and (nr, nc) not in group:
                    stack.append((nr, nc))
        return group

    black_score = 0
    white_score = 0
    visited = set()

    for i in range(size):
        for j in range(size):
            if (i, j) not in visited:
                if board[i][j] == 'B':
                    black_score += 1  # Черный камень добавляется к счету
                elif board[i][j] == 'W':
                    white_score += 1  # Белый камень добавляется к счету
                elif board[i][j] == '.':
                    # Проверяем территории
                    group = get_group(i, j)
                    around_color = set()
                    for r, c in group:
                        visited.add((r, c))
                        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nr, nc = r + dr, c + dc
                            if is_within_bounds(nr, nc) and board[nr][nc] != board[i][j]:
                                around_color.add(board[nr][nc])
                    if around_color == {"W"}:
                        white_score += len(group)
                    elif around_color == {"B"}:
                        black_score += len(group)


    return black_score, white_score
