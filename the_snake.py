from core.consts import (
    BOARD_BACKGROUND_COLOR,
    DOWN, LEFT, RIGHT, UP,
    GRID_HEIGHT, GRID_WIDTH, GRID_SIZE,
    SCREEN_HEIGHT, SCREEN_WIDTH,
)
from core.game import Game

from objects.apple import Apple
from objects.game import GameObject
from objects.snake import Snake

import pygame

__all__ = (
    'GameObject', 'Apple', 'Snake',
    'BOARD_BACKGROUND_COLOR',
    'DOWN', 'UP', 'LEFT', 'RIGHT',
    'GRID_HEIGHT', 'GRID_WIDTH', 'GRID_SIZE',
    'SCREEN_HEIGHT', 'SCREEN_WIDTH',
    'clock',
    'handle_keys',
    'main',
    'screen',
)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
clock = pygame.time.Clock()


def handle_keys(game: Game, snake: Snake):
    """Обрабатывает нажатия клавиш."""
    Game.handle_keys(game, snake)


def main():
    """Основная функция для инициаации."""
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
