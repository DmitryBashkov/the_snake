
from core.game import Game
import pygame


def main():
    '''Основная функция для инициаации.'''

    # Инициализация PyGame:
    pygame.init()
    clock = pygame.time.Clock()

    # Инициализация Game
    game = Game()

    while True:
        clock.tick(20)
        game.turn()
        pygame.display.update()


if __name__ == '__main__':
    main()
