from random import randrange


class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pole = [[Cell() for _ in range(self.N)] for _ in range(self.N)]
        self.init()

    def count_mines(self, i, j):
        mines_counter = 0
        for row in range(i-(not i == 0), i+(not i == self.N-1)+1):
            for col in range(j - (not j == 0), j + (not j == self.N - 1) + 1):
                if row == i and col == j:
                    continue
                if self.pole[row][col].mine:
                    mines_counter += 1
        return mines_counter

    def create_mines(self):
        mine_set = set()
        while len(mine_set) < self.M:
            temp_mine = randrange(self.N*self.N)
            if temp_mine not in mine_set:
                self.pole[temp_mine // self.N][temp_mine % self.N].mine = True
                mine_set.add(temp_mine)

    def init(self):
        self.create_mines()
        for i in range(self.N):
            for j in range(self.N):
                if not self.pole[i][j].mine:
                    self.pole[i][j].around_mines = self.count_mines(i, j)

    def show(self):
        for row in self.pole:
            print(*['#' if not cell.fl_open else cell.around_mines if not cell.mine else 'M' for cell in row])


pole_game = GamePole(10, 12)
