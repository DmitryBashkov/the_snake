from core.consts import (
    BOARD_BACKGROUND_COLOR,
    DOWN,
    GRID_HEIGHT,
    GRID_SIZE,
    GRID_WIDTH,
    LEFT,
    RIGHT,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    UP,
)
from core.game import Game
from objects.apple import Apple
from objects.game import GameObject
from objects.snake import Snake
import pygame

__all__ = (
    'Apple',
    'BOARD_BACKGROUND_COLOR',
    'DOWN',
    'GameObject',
    'GRID_HEIGHT',
    'GRID_SIZE',
    'GRID_WIDTH',
    'LEFT',
    'RIGHT',
    'SCREEN_HEIGHT',
    'SCREEN_WIDTH',
    'Snake',
    'UP',
    'clock',
    'handle_keys',
    'main',
    'screen',
)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
clock = pygame.time.Clock()


def handle_keys(snake):
    '''Обрабатывает нажатия клавиш.'''
    Game.handle_keys(None, snake)


def main():
    '''Основная функция для инициаации.'''

    pygame.init()
    game = Game()
    game.run()

    while game.running:
        clock.tick(game.speed.value)

        if not game.tick():
            break

    pygame.quit()


if __name__ == '__main__':
    main()
