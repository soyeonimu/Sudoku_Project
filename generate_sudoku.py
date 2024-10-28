def generate_sudoku(solved_board):
    """완성된 스도쿠 퍼즐에서 일부 숫자를 제거하여 퍼즐을 반환합니다."""
    board = [row[:] for row in solved_board]  # 해결된 보드를 복사

    # 몇 개의 숫자를 제거하여 퍼즐 생성
    for _ in range(30):  # 30개의 빈 칸 만들기
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        while board[row][col] == 0:  # 이미 빈 칸인 경우 반복
            row = random.randint(0, 8)
            col = random.randint(0, 8)
        board[row][col] = 0  # 빈 칸으로 설정
    return board

# 예시 보드 (해결할 스도쿠 퍼즐)
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

# 스도쿠 해결 시도
solved_board = solve_sudoku(board)

# 구멍이 뚫린 퍼즐 생성 및 출력
generated_board = generate_sudoku(solved_board)
print_board(generated_board)
