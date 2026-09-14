
from core.game import Game
import pygame


def main():
    '''Основная функция для инициаации.'''

    # Инициализация PyGame:
    pygame.init()

    # Инициализация Game
    game = Game()

    # Запуск игры
    game.run()

    while game.running:

        # Если игра возвращает False, то выходим из цикла
        if not game.tick():
            break

    pygame.quit()


if __name__ == '__main__':
    main()
