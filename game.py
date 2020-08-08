import sys
import time
import copy

WAIT_TIME = 0.5  # in seconds
LIVE_CELL = 0


def read_seed(file_path):
    with open(file_path, "r") as seed:
        input_file = seed.readlines()

        index = 0

        # read magic number
        while "P2" not in input_file[index]:
            index += 1
        index += 1

        # skip comments
        while "#" in input_file[index]:
            index += 1

        # skip dimensions
        index += 1

        max_val = int(input_file[index])

        index += 1

        matrix = []
        for line in input_file[index:]:
            # assuming that each pixel is separated by a single space
            matrix.append([int(x) for x in line.strip().split(" ")])

        return max_val, matrix


def print_board(current_board):
    print("--------------------")
    for line in current_board:
        for column in line:
            print(f"{column:1}", end="")
        print()


def evolve(current_board, dead_cell_value):
    new_board = copy.deepcopy(current_board)

    for i, line in enumerate(current_board):
        for j, column in enumerate(line):
            live_neighbours = 0
            # line above the cell
            if i > 0 and j > 0 and current_board[i - 1][j - 1] == 0:
                live_neighbours += 1
            if i > 0 and current_board[i - 1][j] == 0:
                live_neighbours += 1
            if i > 0 and j < len(line) - 1 and current_board[i - 1][j + 1] == 0:
                live_neighbours += 1

            # same line as cell
            if j > 0 and current_board[i][j - 1] == LIVE_CELL:
                live_neighbours += 1
            if j < len(line) - 1 and current_board[i][j + 1] == LIVE_CELL:
                live_neighbours += 1

            # line below the cell
            if i < len(current_board) - 1 and j > 0 and current_board[i + 1][j - 1] == LIVE_CELL:
                live_neighbours += 1
            if i < len(current_board) - 1 and current_board[i + 1][j] == LIVE_CELL:
                live_neighbours += 1
            if i < len(current_board) - 1 and j < len(line) - 1 and current_board[i + 1][j + 1] == LIVE_CELL:
                live_neighbours += 1

            # death by underpopulation or overpopulation
            if current_board[i][j] == LIVE_CELL:
                if live_neighbours == 2 or live_neighbours == 3:
                    new_board[i][j] = LIVE_CELL
                else:
                    new_board[i][j] = dead_cell_value

            # reproduction
            if current_board[i][j] != LIVE_CELL and live_neighbours == 3:
                new_board[i][j] = LIVE_CELL

    return new_board


def is_game_over(current_board):
    for line in current_board:
        for column in line:
            if column == LIVE_CELL:
                return False

    return True


def print_usage():
    print("usage: game.py <path_to_pgm_seed>")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_usage()
        exit(1)

    dead_cell_value, board = read_seed(sys.argv[1])

    print_board(board)
    while not is_game_over(board):
        board = evolve(board, dead_cell_value)
        print_board(board)
        time.sleep(WAIT_TIME)

    print("Game Over")
