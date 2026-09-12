
from core.game import Game
from core.renderer import Renderer
import pygame


def main():
    '''Основная функция для инициаации.'''

    # Инициализация PyGame:
    pygame.init()

    # Инициализация Game
    game = Game()

    # Инициализация рендера
    renderer = Renderer()

    # Запуск игры
    game.run()

    while game.running:

        # Если игра возвращает False,
        # то завершаем текущий цикл
        # с game.running = False
        if not game.tick():
            continue

        # Обновляем графику
        renderer.update


if __name__ == '__main__':
    main()
