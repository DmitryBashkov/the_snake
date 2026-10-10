"""Пожалуйста, примите во внимание,
что текущая версия этого the_snake.py на костылях,
чтобы пройти тесты. В частности, тут импортированы импорты,
которые не используются в коде.
Основной рабочий код находится в ветке pracaticum
"""

import pygame

from core.consts import (BOARD_BACKGROUND_COLOR, GRID_HEIGHT, GRID_SIZE,
                         GRID_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH)
from core.game import Game
from objects.apple import Apple
from objects.game import GameObject
from objects.snake import Snake

__all__ = (
    'GameObject', 'Apple', 'Snake',
    'BOARD_BACKGROUND_COLOR',
    'GRID_HEIGHT', 'GRID_WIDTH', 'GRID_SIZE',
    'SCREEN_HEIGHT', 'SCREEN_WIDTH',
    'clock',
    'main',
    'screen',
)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
clock = pygame.time.Clock()


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
    raise SystemExit


if __name__ == '__main__':
    main()
