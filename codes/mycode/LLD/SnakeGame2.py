import random

import pygame as pygame


class Snake:
    def __init__(self):
        self.body = [(0, 0)]
        self.direction = "up"

    def move(self):
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.body.insert(0, new_head)
        if new_head in self.body[1:]:
            self.die()

    def die(self):
        print("Game over!")
        exit()

    def eat(self):
        self.body.append((0, 0))

class Food:
    def __init__(self):
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)

def main():
    snake = Snake()
    food = Food()

    while True:
        snake.move()

        if snake.body[0] == food.x and snake.body[1] == food.y:
            snake.eat()
            food = Food()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.direction = "up"
                elif event.key == pygame.K_DOWN:
                    snake.direction = "down"
                elif event.key == pygame.K_LEFT:
                    snake.direction = "left"
                elif event.key == pygame.K_RIGHT:
                    snake.direction = "right"

        pygame.display.update()

if __name__ == "__main__":
    main()