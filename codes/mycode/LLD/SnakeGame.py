class Snake:
    def __init__(self, x, y):
        self.body = [[x, y]]  # body length is 1 unit
        self.killed = False

    def move(self, board, dir):
        cur_x, cur_y = self.body[-1]
        if [cur_x + dir[0], cur_y + dir[1]] in self.body:
            self.die()  # hit itself
        if not (0 <= cur_x + dir[0] < Game.LEN_ and 0 <= cur_y + dir[1] < Game.WIDTH_):
            self.die()  ## hit the wall
        if board[cur_x + dir[0]][cur_y + dir[1]]:  # is food
            self.body.append([cur_x + dir[0]][cur_y + dir[1]])
        self.body[0][0] += dir[0]
        self.body[0][1] += dir[1]  #

    def die(self):
        print("Died")
        self.killed = True

    def isKilled(self):
        return self.killed


class Wall:
    pass


class Game:
    board = []
    LEN_ = 10
    WIDTH_ = 10
    DIR = {"up": [-1, 0], "down": [1, 0], "right": [0, 1], "left": [0, -1]}  # enum allowed directions

    def __init__(self):
        # initiliaze the board and snake
        self.board = [[0] * Game.WIDTH_ for _ in range(Game.LEN_)]
        self.snake = Snake(0, 0)

    def addFood(self, x, y):
        self.board[x][y] = 1

    def isGameOver(self):
        if self.snake.isKilled() == True:
            exit(1)

    def move(self, dir):
        self.snake.move(self.board, Game.DIR[dir])
        self.isGameOver()

    def undo(self):
        pass

    def reset(self):
        self.__init__()


if __name__ == '__main__':
    game = Game()
    game.addFood(1, 5)
    game.addFood(4, 5)
    game.addFood(5, 1)
    game.move("right")
    game.move("right")
    game.move("right")
    game.move("right")
