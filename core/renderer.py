import pygame

from core.consts import (BOARD_BACKGROUND_COLOR, BORDER_COLOR, GAME_NAME,
                         GRID_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH)
from objects.game import GameObject


class Renderer():
    """Класс для отрисовки объектов на экране."""

    screen: pygame.Surface

    def __init__(self):
        # Настройка игрового окна:
        self.screen = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT),
            0,
            32)

        # Заголовок окна игрового поля:
        pygame.display.set_caption(GAME_NAME)

    def clear(self):
        """Очищает экран, заливая его цветом фона."""
        self.screen.fill(BOARD_BACKGROUND_COLOR)

    def _draw_element(self,
                      position: tuple[int, int],
                      color: tuple[int, int, int],

                      # fade используется для прорисовки фона
                      # у последнего элемента змейки
                      fade: bool = False) -> None:
        """Рисует отдельную позицию объекта."""
        rect = pygame.Rect(position, (GRID_SIZE, GRID_SIZE))

        if fade:
            pygame.draw.rect(
                self.screen,
                BOARD_BACKGROUND_COLOR,
                rect,
            )

        else:
            pygame.draw.rect(self.screen, color, rect)
            pygame.draw.rect(
                self.screen,
                BORDER_COLOR,
                rect, 1,
            )

    def _draw(self,
              positions: list[tuple[int, int]],
              color: tuple[int, int, int]) -> None:
        """Рисует игровой объект"""
        for position in positions:
            self._draw_element(position, color)

    def update(self):
        """Обновляет экран. Вызывается после отрисовки всех объектов."""
        pygame.display.update()

    def draw_objects(self, game_objects: list[GameObject]) -> None:
        """Рисует все игровые объекты"""
        for object in game_objects:
            self._draw(object.positions, object.body_color)
