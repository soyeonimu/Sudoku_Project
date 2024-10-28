def solve_sudoku(board):
    """주어진 스도쿠 퍼즐을 해결합니다. 해결할 수 없는 경우 메시지를 출력합니다."""

    def is_valid(row, col, num):
        """주어진 위치에 숫자를 넣을 수 있는지 확인합니다."""
        # 행, 열 확인
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        # 3x3 박스 확인
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if board[i][j] == num:
                    return False
        return True  # 유효한 경우

    def backtrack():
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:  # 빈 공간을 찾기
                    for num in range(1, 10):  # 1-9 숫자 시도
                        if is_valid(row, col, num):
                            board[row][col] = num  # 숫자 배치
                            if backtrack():  # 재귀적으로 해결 시도
                                return True
                            board[row][col] = 0  # 실패 시 초기화
                    return False  # 모든 숫자를 시도했지만 실패
        return True  # 성공적으로 해결됨

    if backtrack():  # 해결이 가능하다면
        return board
    else:
        return None  # 해결할 수 없는 경우

# 스도쿠 퍼즐 예시
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# 현재 보드 출력
print("현재 스도쿠 퍼즐:")
print_board(board)

# 스도쿠 해결 시도
print("\n해결된 스도쿠 퍼즐:")
solved_board = solve_sudoku(board)
if solved_board:
    print_board(solved_board)
else:
    print("해결할 수 없는 스도쿠 퍼즐입니다.")