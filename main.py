numbers = [0, 56, 39, 4, 52, 7, 73, 57, 65, 13, 3, 72, 69, 96, 18, 9, 49, 83, 24, 31, 12, 64, 29, 21, 80, 71, 66, 95, 2,
           62, 68, 46, 11, 33, 74, 88, 17, 15,
           5, 6, 98, 30, 51, 78, 76, 75, 28, 53, 87, 48, 20, 22, 55, 86, 82, 90, 47, 19, 25, 1, 27, 60, 94, 38, 97, 58,
           70, 10, 43, 40, 89, 26, 34, 32, 23,
           45, 50, 91, 61, 44, 35, 85, 63, 16, 99, 92, 8, 36, 81, 84, 79, 37, 93, 67, 59, 54, 41, 77, 42, 14]


def make_boards():
    with open("day-4-input.txt") as file:
        lines = file.readlines()

    rows = []

    for line in lines:
        if len(line) > 1:
            rows.append(line.split())
    num_boards = int(len(rows) / 5)
    boards = []
    for _ in range(num_boards):
        boards.append([])
    c = 0
    for x in range(len(rows)):
        if x != 0 and x % 5 == 0:
            c += 1
        boards[c].append(rows[x])

    return boards


def is_winner(board):
    for row in range(5):
        if board[row][0] == "x" and board[row][1] == "x" and board[row][2] == "x" and board[row][3] == "x" and \
                board[row][4] == "x":
            return True

    for column in range(5):
        if board[0][column] == "x" and board[1][column] == "x" and board[2][column] == "x" and board[3][column] == "x" \
                and board[4][column] == "x":
            return True


def calc_score(board, last_number):
    sum_total = 0
    for row in range(5):
        for column in range(5):
            if board[row][column] != "x":
                sum_total += int(board[row][column])
    return sum_total * last_number


def first_winner(boards):
    for number in numbers:
        for c in range(len(boards)):
            for row in range(5):
                for column in range(5):
                    if boards[c][row][column] == str(number):
                        boards[c][row][column] = "x"
            if len(boards) == 1 and is_winner(boards[c]):
                return calc_score(boards[c], number)
            elif len(boards) != 1 and is_winner(boards[c]):
                return c, calc_score(boards[c], number)


def last_winner(boards):
    while len(boards) != 1:
        board_number = first_winner(boards)[0]
        boards.pop(board_number)
    print(f"The final board's final score is {first_winner(boards)}.")


print(f"The first board's final score is {first_winner(make_boards())[1]}.")

last_winner(make_boards())
