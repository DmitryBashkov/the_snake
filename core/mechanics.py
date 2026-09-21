import pygame
from core.consts import (
    DEFAULT_SPEED
)


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
