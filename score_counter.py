def count_chinese_score(board):
    size = len(board)

    def is_within_bounds(row, col):
        """Проверка, что координаты находятся в пределах доски"""
        return 0 <= row < size and 0 <= col < size

    def get_group(row, col):
        """Получение группы связанных камней|пустых полей"""
        _color = board[row][col]
        connected_stones = set()
        stack = [(row, col)]
        while stack:
            current_row, current_col = stack.pop()
            if (current_row, current_col) in connected_stones:
                continue
            connected_stones.add((current_row, current_col))
            for delta_row, delta_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_col = current_row + delta_row, current_col + delta_col
                if (
                        is_within_bounds(new_row, new_col) and
                        board[new_row][new_col] == _color and
                        (new_row, new_col) not in connected_stones
                ):
                    stack.append((new_row, new_col))
        return connected_stones

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
