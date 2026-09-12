from objects.game import GameObject
from objects.snake import Snake
from objects.apple import Apple
from objects.wall import Wall
from core.mechanics import Speed
from core.renderer import Renderer
import pygame


class Game():
    '''Класс для управления игрой.'''

    def __init__(self):
        self._snake = Snake()
        self._game_objects: set[GameObject] = set()
        self._game_objects_to_remove: set[GameObject] = set()
        self._running = False
        self._gave_over_on_interception: bool
        self.speed = Speed()
        self.clock = pygame.time.Clock()
        self.renderer = Renderer()
        self._game_objects.add(self._snake)
        self.tick()

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

        self.clock.tick(self.speed.value)

        # Для масштабируемости:
        # все объекты, которые должны двигаться, делают шаг
        # В нашем случае это только замейка и все
        for object in self._game_objects:
            object.move()
            self.renderer.draw(object.positions, object.body_color)

        # Определяем, есть ли столкновения змейки
        # с каким-либо объектом после движения
        interception_object = self._has_interception()

        # Если есть столкновение
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

                wall = Wall(self._snake.eat(interception_object))

                if wall:
                    self.add_game_objects_to_list(wall)

            # Добавляем объект в список на удаление
            self.remove_object(interception_object)

        # Удаляем все объекты из списка на удаление
        self.remove_game_objects_from_list()

        return True

    def change_snake_direction(self, new_direction: tuple[int, int]) -> None:
        '''Меняет направление '''
        self._snake.update_direction(new_direction)

    def _has_interception(self) -> GameObject | None:
        '''Возвращает объект, с которым произошло столкноввение.
        None, если столкновения нет.'''

        for object in self._game_objects:
            if not isinstance(object, Snake):
                if self._snake.head == object.head:
                    return object
            else:
                if self._snake.head in self._snake.positions:
                    return self._snake
        return None

    def _game_over(self):
        pass

    def add_game_objects_to_list(self, obj: GameObject) -> None:
        '''Добавляет новый игровой объект в список.'''
        self._game_objects.add(obj)

    def remove_game_objects_from_list(self) -> None:
        '''Удаляет ненужные игровые объекты из списка.'''
        for object in self._game_objects_to_remove:
            if object in self._game_objects:
                self._game_objects.discard(object)

                # Заодно освободим память на всякий случай
                del object

        self._game_objects_to_remove.clear()

    def remove_object(self, obj: GameObject):
        '''Вносит удаляемый объект в список на удаление.'''
        self._game_objects_to_remove.add(obj)
