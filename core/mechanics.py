import pygame

from core.consts import DEFAULT_SPEED

# Настройка времени:
clock = pygame.time.Clock()


class Speed:
    """Скорость движения змейки."""

    _speed: int

    def __init__(self) -> None:
        self._speed = DEFAULT_SPEED

    def inc(self, value: int = 20) -> None:
        """Увеличение скорости. По дефолту на +20"""
        self._speed += value

    def dec(self, value: int = 20) -> None:
        """Уменьшение скорости. По дефолту на -20"""
        self._speed -= value

    def set_default(self) -> None:
        """Устанавливаем дефолтную скорость игры"""
        self._speed = DEFAULT_SPEED

    def __int__(self) -> int:
        """Возвращает скорость в виде int"""
        return self._speed

    @property
    def value(self) -> int:
        """Свойство. Возвращает скорость в виде int"""
        return self._speed


speed = Speed()
