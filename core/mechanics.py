import pygame
from core.consts import (
    UP, DOWN, LEFT, RIGHT,
    DEFAULT_SPEED
)

from objects.snake import Snake

# Настройка времени:
clock = pygame.time.Clock()


class Speed():
    '''Скорость движения змейки'''

    _speed: int

    def __init__(self):
        self._speed = 20

    def inc(self, value: int = 20):
        '''Увеличение скорости. По дефолту на +20'''
        self._speed += value

    def dec(self, value: int = 20):
        '''Уменьшение скорости. По дефолту на -20'''
        self._speed -= value

    def set_default(self):
        '''Устанавливаем дефолтную скорость игры'''
        self._speed = DEFAULT_SPEED

    def __int__(self):
        return self._speed

    @property
    def value(self):
        return self._speed


speed = Speed()


def handle_keys(snake: Snake):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != UP:
                snake.update_direction(UP)
            elif event.key == pygame.K_DOWN and snake.direction != DOWN:
                snake.update_direction(DOWN)
            elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
                snake.update_direction(LEFT)
            elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                snake.update_direction(RIGHT)
