from objects.game import GameObject
from objects.snake import Snake
from objects.apple import Apple
from objects.wall import Wall
from core.mechanics import Speed
from core.renderer import Renderer
from core.consts import (
    UP, DOWN, LEFT, RIGHT,
    MAX_APPLES
)
import pygame


class Game():
    '''Класс для управления игрой.'''

    def __init__(self):

        self._game_objects: GameObjects = GameObjects()
        self._running = False
        self.speed = Speed()
        self.clock = pygame.time.Clock()
        self.renderer = Renderer()

        self._snake = Snake()
        self._game_objects.add_object(self._snake)

        for _ in range(MAX_APPLES):
            self._game_objects.add_object(Apple())

    def run(self):
        ''' Устанавливаем _running = True'''
        self._running = True

    def stop(self):
        ''' Устанавливаем _running = False'''
        self._running = False

    @property
    def running(self):
        return self._running

    def tick(self) -> bool:
        # TODO: добавить обработку lifetime
        # TODO: добавить обработку столкновений с границами

        self.clock.tick(self.speed.value)

        self.handle_keys(self._snake)

        # Для масштабируемости:
        # все объекты, которые должны двигаться, делают шаг
        # В нашем случае это только замейка и все
        self._game_objects.move_objects()

        self._game_objects.dec_lifetime()

        # Определяем, есть ли столкновения змейки
        # с каким-либо объектом после движения
        self._handle_interception()

        self.renderer.clear()
        self.renderer.draw_objects(self._game_objects.objects)

        self.renderer.update()

        return True

    def _handle_interception(self):
        '''Обрабатывает столкновения змейки с объектами.'''

        interception_object = self._has_interception()

        if interception_object:

            # Есть ли столкновение с объектами,
            # после которых игра заканчивается
            if interception_object.is_game_over_on_interception:

                # Заканчиваем игру, останавливаем
                self._game_over()
                self.stop()
                return False

            # В остальных случаях проверяем, с яблоком ли столкновение
            elif isinstance(interception_object, Apple):

                interception_object.detect_type()

                wall = self._snake.eat(interception_object)
                if wall:
                    wall = Wall(wall)
                    self._game_objects.add_object(wall)

                self._game_objects.remove_object(interception_object)
                self._apple = Apple()
                self._game_objects.add_object(self._apple)

            return True

        else:
            return False

    def change_snake_direction(self, new_direction: tuple[int, int]) -> None:
        '''Меняет направление '''
        self._snake.update_direction(new_direction)

    def _has_interception(self) -> GameObject | None:
        '''Возвращает объект, с которым произошло столкноввение.
        None, если столкновения нет.'''

        for object in self._game_objects.objects:
            if not isinstance(object, Snake):
                if self._snake.head in object.positions:
                    return object
            else:
                if self._snake.head in self._snake.positions[1:]:
                    return self._snake
        return None

    def _game_over(self):
        pass

    def handle_keys(self, snake: Snake):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != DOWN:
                    snake.update_direction(UP)
                elif event.key == pygame.K_DOWN and snake.direction != UP:
                    snake.update_direction(DOWN)
                elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
                    snake.update_direction(LEFT)
                elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                    snake.update_direction(RIGHT)


class GameObjects():

    def __init__(self):
        self._objects: list[GameObject] = []
        self._used_positions: list[tuple[int, int]] = []

    @property
    def objects(self) -> list[GameObject]:
        '''Возвращает все игровые объекты, которые есть в игре.'''
        return self._objects

    @property
    def used_positions(self) -> list[tuple[int, int]]:
        '''Возвращает список всех позиций на поле всех игровых объектов.'''
        positions = list[tuple[int, int]]()

        for object in self._objects:
            positions.append(*object.positions)
        return positions

    def add_object(self, obj: GameObject) -> None:
        '''Добавляет новый игровой объект в список.'''
        self._objects.append(obj)
        # TODO при столкновении со стеной, append получает несколько аргументов
        self._used_positions.extend(obj.positions)

    def remove_object(self, obj: GameObject) -> None:
        '''Удаляет игровой объект из списка.'''
        if obj not in self._objects:
            return
        else:
            self._objects.remove(obj)
            self._used_positions.remove(*obj.positions)

    def move_objects(self) -> None:
        '''Двигает все объекты.'''
        for object in self._objects:
            object.move()

    def dec_lifetime(self) -> None:
        '''Уменьшает lifetime всех объектов на 1.'''
        for object in self._objects:

            # еще живой объект
            if object.life_time > 0:
                object.dec_lifetime()

            # объект, lifetime которого закончился, удаляем из игрs
            elif object.life_time == 0:
                self.remove_object(object)

            # объект, который не имеет lifetime (в данном случае змейка)
            elif object.life_time == -1:
                pass
