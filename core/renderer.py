import pygame
from core.consts import (
    SCREEN_HEIGHT, SCREEN_WIDTH,
    GAME_NAME,
    GRID_SIZE,
    BORDER_COLOR, BOARD_BACKGROUND_COLOR
)


class Renderer():

    screen: pygame.Surface

    def __init__(self):
        # Настройка игрового окна:
        self.screen = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT),
            0,
            32)

        # Заголовок окна игрового поля:
        pygame.display.set_caption(GAME_NAME)

    def _draw_element(self,
                      position: tuple[int, int],
                      color: tuple[int, int, int],
                      fade: bool = False) -> None:
        '''Рисует отдельную позицию объекта.'''

        rect = pygame.Rect(position, (GRID_SIZE, GRID_SIZE))

        if fade:
            pygame.draw.rect(
                self.screen,
                BOARD_BACKGROUND_COLOR,
                rect
            )

        else:
            pygame.draw.rect(self.screen, color, rect)
            pygame.draw.rect(
                self.screen,
                BORDER_COLOR,
                rect, 1
            )

    def draw(self,
             positions: list[tuple[int, int]],
             color: tuple[int, int, int]) -> None:
        '''Рисует игровой объект'''
        for position in positions:
            self._draw_element(position, color)
