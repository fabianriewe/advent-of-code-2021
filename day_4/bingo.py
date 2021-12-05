from typing import List

with open("./input.txt") as file:
    lines = file.readlines()


class BingoCard:
    won = False
    winning_number = None

    def __init__(self, rows: List[List[int]]):
        self.rows = rows

    def _check_row(self) -> bool:
        for row in self.rows:
            if sum(row) == -5:
                return True

        return False

    def _check_col(self) -> bool:
        for index in range(len(self.rows)):
            col = []
            for row in self.rows:
                col.append(row[index])

            if sum(col) == -5:
                return True

        return False

    def add_draw(self, number: int):

        for row in range(len(self.rows)):
            for col in range(len(self.rows[0])):
                if self.rows[row][col] == number:
                    self.rows[row][col] = -1

        self.won = self._check_col() or self._check_row()
        self.winning_number = number

    def sum_of_umarked(self) -> int:
        sum = 0
        for row in self.rows:
            for number in row:
                if number != -1:
                    sum += number

        return sum


draws = lines[0].strip().split(",")

print(draws)
boards = []
board = []
for line in lines[2::]:
    line = line.strip().replace("  ", " ").split(" ")
    if len(line) == 5:
        line = list(map(lambda e: int(e), line))
        board.append(line)
    else:
        boards.append(board)
        board = []

boards.append(board)
cards = []
for board in boards:
    cards.append(BingoCard(board))

won_cards = []
for number in draws:
    number = int(number)
    for i, card in enumerate(cards):
        if not card.won:
            card.add_draw(number)
        else:
            if card not in won_cards:
                won_cards.append(card)
                print("Card", i, "won! Result:", card.sum_of_umarked() * card.winning_number, card.winning_number)
                # 14093
                if len(won_cards) == len(cards):
                    exit(0)
