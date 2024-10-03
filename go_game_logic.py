from logging_setup import game_logger
from score_counter import count_chinese_score
from configuration import BoardConfig


class GoGameLogic:
    # Переменные для очков
    black_score = 0
    white_score = 0
    pass_count = 0  # Количество подряд идущих пасов
    game_over = False

    def __init__(self, size, bord_config: BoardConfig, board=None, fake=False):
        self.size = size
        self.fake = fake
        self.bordConfig = bord_config
        # Инициализация доски
        self.board = [['.' for _ in range(size)] for _ in range(size)] \
            if board is None else board
        self.current_player = 'B'  # Начинает игрок 'B'

    def is_in_bounds(self, row, col):
        """Проверка, что координаты находятся в пределах доски"""
        return 0 <= row < self.size and 0 <= col < self.size

    def place_stone(self, row, col):
        """Размещение камня на доске и проверка захвата камней противника"""
        if not self.is_in_bounds(row, col) or self.board[row][col] != '.':
            return False

        if not self.fake:
            game_logger.info(f"{self.current_player}: ({row}, {col})")
        self.pass_count = 0

        # Помещение камня на доску
        self.board[row][col] = self.current_player

        # Конец игры, если вся доска заполнена камнями
        sum_empty = sum(row.count('.') for row in self.board)
        if sum_empty == 0:
            self.end_game()

        # Проверка на захват камней противника
        self.check_capture(row, col, self.current_player)

        # Смена текущего игрока
        self.current_player = 'W' if self.current_player == 'B' else 'B'
        self.check_capture(row, col, self.current_player)

        return True

    def pass_move(self):
        """Игрок совершает пас."""
        self.pass_count += 1
        if self.current_player == 'B':
            self.black_score += 1
        else:
            self.white_score += 1
        self.current_player = 'W' if self.current_player == 'B' else 'B'
        if self.pass_count >= 2:
            self.end_game()

    def check_capture(self, row, col, opponent_color):
        """Проверка и захват камней противника"""

        def get_group(start_row, start_col):
            """Получение группы связанных камней"""
            _color = self.board[start_row][start_col]
            connected_stones = set()
            stack = [(start_row, start_col)]
            while stack:
                group_row, group_col = stack.pop()
                if (group_row, group_col) in connected_stones:
                    continue
                connected_stones.add((group_row, group_col))
                for delta_row, delta_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_row, new_col = group_row + delta_row, group_col + delta_col
                    if (self.is_in_bounds(new_row, new_col)
                            and self.board[new_row][new_col] == _color
                            and (new_row, new_col) not in connected_stones):
                        stack.append((new_row, new_col))
            return connected_stones

        def has_liberties(stone_group):
            """Проверка наличия свободных точек у группы"""
            for group_row, group_col in stone_group:
                for delta_row, delta_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_row, new_col = group_row + delta_row, group_col + delta_col
                    if self.is_in_bounds(new_row, new_col) and self.board[new_row][new_col] == '.':
                        return True
            return False

        is_delite = False

        # Проверка захвата камней противника
        for r, c in get_group(row, col):
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if self.is_in_bounds(nr, nc) and self.board[nr][nc] == opponent_color:
                    group = get_group(nr, nc)
                    if not has_liberties(group):
                        is_delite = True
                        if self.current_player == 'B':
                            self.black_score += len(group)
                        else:
                            self.white_score += len(group)
                        for gr, gc in group:
                            self.board[gr][gc] = '.'  # Удаление захваченных камней

        if is_delite:
            return
        # Самострел
        group = get_group(row, col)
        if not has_liberties(group):
            for gr, gc in group:
                self.board[gr][gc] = '.'  # Удаление захваченных камней

    def end_game(self):
        """Завершение игры и подсчет очков."""
        self.game_over = True
        self.black_score = count_chinese_score(self.board)[0]
        self.white_score = count_chinese_score(self.board)[1]
        print("Игра закончена. Подсчет очков...")
        print("Очки черных:", self.black_score)
        print("Очки белых:", self.white_score)
