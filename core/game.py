from random import randint

import pygame

from core.consts import (DOWN, GRID_HEIGHT, GRID_SIZE, GRID_WIDTH, LEFT,
                         MAX_APPLES, RIGHT, UP)
from core.mechanics import Speed
from core.renderer import Renderer
from objects.apple import Apple
from objects.game import GameObject
from objects.snake import Snake
from objects.wall import Wall


class Game:
    """Класс для управления игрой."""

    def __init__(self):

        self._game_objects: GameObjects = GameObjects()
        self._running = False
        self.speed = Speed()
        self.clock = pygame.time.Clock()
        self.renderer = Renderer()

        self._snake = Snake()
        self._game_objects.add_object(self._snake)

        for _ in range(MAX_APPLES):
            self._game_objects.add_object(Apple(self.gen_rand_pos()))

    def run(self):
        """Устанавливаем _running = True."""
        self._running = True

    def stop(self):
        """Устанавливаем _running = False"""
        self._running = False

    @property
    def running(self):
        """Возвращает True, если игра запущена, иначе False."""
        return self._running

    def tick(self) -> bool:
        """Один игровой цикл. Возвращает True, если игра продолжается"""
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
        """Обрабатывает столкновения змейки с объектами."""
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

                is_wall = self._snake.eat(interception_object)
                if is_wall:
                    wall = Wall(is_wall)
                    self._game_objects.add_object(wall)

                self._game_objects.remove_object(interception_object)
                self._apple = Apple(self.gen_rand_pos())
                self._game_objects.add_object(self._apple)

            return True

        return False

    def _has_interception(self) -> GameObject | None:
        """Возвращает объект, с которым произошло столкноввение.
        None, если столкновения нет.
        """
        for obj in self._game_objects.objects:
            if not isinstance(obj, Snake):
                if self._snake.head in obj.positions:
                    return obj
            else:
                if self._snake.head in self._snake.positions[1:]:
                    return self._snake
        return None

    def _game_over(self):
        """Останавливает игру."""
        self.stop()

    def handle_keys(self, snake: Snake):
        """Обрабатывает нажатия клавиш."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            if event.type == pygame.KEYDOWN:

                """
                дальше очень хреновая логика,
                которая меняет направление змейки в зависимости от того,
                в каком состоянии она находится (reverse = True/False)
                Вдобавок ей надо проверять, что при реверсе кнопок управления,
                змейка не может двигаться в противоположном направлении
                иначе она столкнется сама с собой
                Такая хуйня, собачка

                И чтобы нас не ругал преподаватель за слишком сложное изложение
                мы попробуем оправдаться новыми функциями
                в классе змейки axis_horizontal и axis_vertical,
                которые возвращают true / false
                и щепоткой кода в update_direction

                Логика такая. Если нажата кнопка,
                и направление змейки не в одной оси с кнопкой,
                то обновляем направление.

                При этом, если включен реверс,
                то направление меняется на противоположное.
                """

                if event.key == pygame.K_UP and not snake.axis_vert:
                    snake.update_direction(DOWN if snake.reverse else UP)
                elif event.key == pygame.K_DOWN and not snake.axis_vert:
                    snake.update_direction(UP if snake.reverse else DOWN)
                elif event.key == pygame.K_LEFT and not snake.axis_horizon:
                    snake.update_direction(RIGHT if snake.reverse else LEFT)
                elif event.key == pygame.K_RIGHT and not snake.axis_horizon:
                    snake.update_direction(LEFT if snake.reverse else RIGHT)

    def gen_rand_pos(self) -> list[tuple[int, int]]:
        """
        Определение случайной позиции для игрового объекта.
        Почему это тут, а не в классе игрового объекта?

        Потому что "ответственность" за генерацию позиции,
        которая не попадает в какой-либо другой объект,
        лежит на уровне игры, а не игрового объекта.
        Игровому объекту необязательно знать о других объектах.
        """
        while True:
            position = [(
                randint(0, GRID_WIDTH) * GRID_SIZE,
                randint(0, GRID_HEIGHT) * GRID_SIZE,
            )]
            if position[0] not in self._game_objects.used_positions:
                return position


class GameObjects:
    """Класс для управления списком игровых объектов.
    Такими, добавление объектов, удаления итд.
    """

    def __init__(self):
        self._objects: list[GameObject] = []
        self._used_positions: list[tuple[int, int]] = []

    @property
    def objects(self) -> list[GameObject]:
        """Возвращает список всех игровых объектов, которые есть в игре."""
        return self._objects

    @property
    def used_positions(self) -> list[tuple[int, int]]:
        """Возвращает список всех позиций на поле всех игровых объектов."""
        positions = list[tuple[int, int]]()

        for obj in self._objects:
            positions.extend(obj.positions)
        return positions

    def add_object(self, obj: GameObject) -> None:
        """Добавляет новый игровой объект в список."""
        self._objects.append(obj)
        self._used_positions.extend(obj.positions)

    def remove_object(self, obj: GameObject) -> None:
        """Удаляет игровой объект из списка."""
        if obj not in self._objects:
            return
        
        self._objects.remove(obj)
        for position in obj.positions:
            if position in self._used_positions:
                self._used_positions.remove(position)

    def move_objects(self) -> None:
        """Двигает все объекты."""
        for obj in self._objects:
            obj.move()

    def dec_lifetime(self) -> None:
        """Уменьшает lifetime всех объектов на 1."""
        for obj in self._objects:

            # еще живой объект
            if obj.life_time > 0:
                obj.dec_lifetime()

            # объект, lifetime которого закончился, удаляем из игрs
            elif obj.life_time == 0:
                self.remove_object(obj)

            # объект, который не имеет lifetime (в данном случае змейка)
            elif obj.life_time == -1:
                pass
