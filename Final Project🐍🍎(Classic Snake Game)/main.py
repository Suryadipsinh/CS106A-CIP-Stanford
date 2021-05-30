"""
Snake Game: (By Suryadipsinh Vaghela)

Welcome to the 'Snake World'! This is my classic 'Snake Game'.

About the Game:
-   The objective is to keep eating ‘Apple’ that appears in random locations to keep increasing your snake size.
-   Player has Keyboard controls provided for navigating Snake on the arena
     🎮  Contorls : ← ↓ ↑ → keys
-   The game goes on until the players’ snake is dead. The score will be displayed at the end of the game.
     o	Snake can die in any of the following scenarios:
        	Hits the wall / boundary
        	Hits itself
"""

import pygame
import time
import random
from pygame.locals import *


class Snake:

    """
        This class defines the properties of a snake object for the game and contains methods for creating the snake,
        dynamically increasing its size and its movements
    """

    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("Graphics/snake_image.jpeg").convert()
        self.direction = 'down'

        self.length = 1
        self.x = [40]
        self.y = [40]

    def draw(self):
        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))

        pygame.display.flip()

    def increase_length(self):
        """
        This method increments the snake size by '1', by adding a block to it.
        """
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    """
       Algorithm to move snake:
        1) The ‘snake head’ is repositioned based on the player controls.
        2) The block following the snake head is programmed to take
        snake head’s previous position in the subsequent frame.
        Similarly, the 3rd block takes the 2nd block position and so on.
    """

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def walk(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == 'up':
            self.y[0] -= 40
        elif self.direction == 'down':
            self.y[0] += 40
        elif self.direction == 'left':
            self.x[0] -= 40
        elif self.direction == 'right':
            self.x[0] += 40

        self.draw()


class Apple:

    """
    This class defines the properties of a Apple object for the game and contains methods for creating the apple,
    moving it the to the random places of the game screen.
    """

    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("Graphics/apple_image.jpg").convert()
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        """
        Method to randomly place a circular 'Apple' anywhere on Game screen.
        """
        self.x = random.randint(1, 24) * 40
        self.y = random.randint(1, 18) * 40


class Game:

    """
    This class defines different Methods for doing following things:
    - Initialising the game
    - Playing background music for game
    - Playing sound while hitting apple as well as itself
    - Adding a background screen
    - Keyboard controls
    - displaying score after game over etc
    """

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake Game by Suryadip")

        pygame.mixer.init()
        self.play_background_music()

        self.screen = pygame.display.set_mode((1000, 780))
        self.snake = Snake(self.screen)
        self.snake.draw()
        self.apple = Apple(self.screen)
        self.apple.draw()

    def play_background_music(self):
        """
        This method will play background music will running the game.
        """
        pygame.mixer.music.load("sound/background_music.mpeg")
        pygame.mixer.music.play(-1, 0)

    def play_sound(self, sound):
        """
        This method will play sound while snake eats apple and while snake hits itself.
        """
        if sound == 'eating_sound':
            sound = pygame.mixer.Sound("sound/Apple_eat.mpeg")
        elif sound == 'crash_sound':
            sound = pygame.mixer.Sound("sound/crash_sound.mp3")
        pygame.mixer.Sound.play(sound)

    def background_screen(self):
        """
        This method is for showing background image for the game.
        """
        bg = pygame.image.load("Graphics/background_image.jpg")
        self.screen.blit(bg, (0, 0))

    def is_collision(self, x_apple, y_apple, x_snake, y_snake):
        if x_apple >= x_snake and x_apple < (x_snake + 40):
            if y_apple >= y_snake and y_apple < (y_snake + 40):
                return True
        return False

    def play(self):
        self.background_screen()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        """
        Method to handle events during the Snake's motion.
        Makes use of 'tags' given to each object to filter out what's overlapping.
        1. Hit apple --> while colliding with apple, increment snake size and move apple
        2. Hit itself --> Check if Snake hit itself or other snake: If yes, game over.
        3. Hit wall --> Check if Snake head went past the wall coordinates: If yes, game over.

        """

        # 1. snake colliding with apple :
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.play_sound("eating_sound")
            self.snake.increase_length()
            self.apple.move()

        # 2. snake colliding with itself :
        for i in range(2, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.play_sound("crash_sound")
                raise Exception("Error Hitting itself")

        # 3. snake colliding with wall/boundaries :
        if not (0 <= self.snake.x[0] <= 1000 and 0 <= self.snake.y[0] <= 800):
            self.play_sound('crash')
            raise Exception("Hitting the wall error")

    def display_score(self):
        """
        Method to position score_board text on the game window
        """
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (200, 200, 200))
        self.screen.blit(score, (850, 10))

    def reset(self):  # will reset the game once the game is over.
        self.snake = Snake(self.screen)
        self.apple = Apple(self.screen)

    def show_game_over(self):
        """
        Method to print final message and show the score.
        at the end the game user would be able to play again the same game by pressing ENTER and
        would be able to exit the game by pressing ESCAPE key.
        """
        self.background_screen()
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game is over! Your score is {self.snake.length}", True, (255, 255, 255))
        self.screen.blit(line1, (200, 300))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.screen.blit(line2, (200, 350))
        pygame.mixer.music.pause()
        pygame.display.flip()

    def run(self):
        """
        Method to bind keyboard inputs on game window to specific functions
        for navigating the snake
        """
        running = True
        pause = False
        # Event loop
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause = False

                    if not pause:
                        if event.key == K_UP:
                            self.snake.move_up()

                        if event.key == K_DOWN:
                            self.snake.move_down()

                        if event.key == K_LEFT:
                            self.snake.move_left()

                        if event.key == K_RIGHT:
                            self.snake.move_right()

                elif event.type == QUIT:
                    running = False

            try:

                if not pause:
                    self.play()

            except Exception:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(0.1)


if __name__ == "__main__":
    game = Game()
    game.run()
