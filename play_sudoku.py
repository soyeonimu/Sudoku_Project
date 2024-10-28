def play_sudoku():
    """사용자에게 스도쿠 게임을 플레이할 기회를 제공합니다."""

    # 빈 보드 생성 및 해결 시도
    board = initialize_board()
    solved_board = solve_sudoku(board)  # 해결된 퍼즐 생성

    if solved_board:
        generated_board = generate_sudoku(solved_board)  # 구멍 뚫린 퍼즐 생성
        print("스도쿠 게임을 시작합니다!")
        print_board(generated_board)  # 초기 구멍 뚫린 보드 출력
        print("=" * 21)  # 문제 아래 구분선 추가

        while True:
            try:
                row = int(input("행을 입력하세요 (1-9): ")) - 1
                col = int(input("열을 입력하세요 (1-9): ")) - 1
                num = int(input("숫자를 입력하세요 (1-9): "))

                # 입력값 검증
                if not (0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9):
                    print("잘못된 입력입니다. 게임을 종료합니다.")
                    print("=" * 21)  # 구분선 추가
                    break

                if generated_board[row][col] != 0:
                    print("이미 숫자가 있는 칸입니다. 게임을 종료합니다.")
                    print("=" * 21)  # 구분선 추가
                    break

                # 유효성 검사
                if (num in generated_board[row] or  # 행 검사
                    any(generated_board[i][col] == num for i in range(9)) or  # 열 검사
                    any(generated_board[r][c] == num for r in range((row // 3) * 3, (row // 3) * 3 + 3)
                                                          for c in range((col // 3) * 3, (col // 3) * 3 + 3))):  # 3x3 박스 검사
                    print("잘못된 이동입니다. 게임을 종료합니다.")
                    print("=" * 21)  # 구분선 추가
                    break

                generated_board[row][col] = num  # 사용자 입력으로 숫자 추가
                print_board(generated_board)  # 업데이트된 보드 출력
                print("=" * 21)  # 구분선 추가

                # 게임 승리 조건
                if all(all(cell != 0 for cell in row) for row in generated_board):
                    print("축하합니다! 스도쿠를 완료했습니다!")
                    print_board(generated_board)
                    break

            except ValueError:
                print("유효하지 않은 입력입니다. 숫자를 입력해야 합니다. 게임을 종료합니다.")
                print("=" * 21)  # 구분선 추가
                break
    else:
        print("해결할 수 없는 스도쿠 퍼즐입니다.")

# 게임 시작
play_sudoku()