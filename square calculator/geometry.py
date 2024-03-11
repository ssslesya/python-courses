import math
from math import pi


def circle_area(radius):
    """
  Вычисляет площадь круга.

  Args:
      radius: Радиус круга.

  Returns:
      Площадь круга.
  """
    if not isinstance(radius, (int, float)):
        raise TypeError("Радиус должен быть числом")
    if radius < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return pi * radius ** 2


def triangle_area(a, b, c):
    """
  Вычисляет площадь треугольника.

  Args:
      a: Длина первой стороны треугольника.
      b: Длина второй стороны треугольника.
      c: Длина третьей стороны треугольника.

  Returns:
      Площадь треугольника.
  """
    if not all(isinstance(side, (int, float)) for side in (a, b, c)):
        raise TypeError("Стороны треугольника должны быть числами")
    if any(side < 0 for side in (a, b, c)):
        raise ValueError("Стороны треугольника не могут быть отрицательными")
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


def is_right_triangle(a, b, c):
    """
  Проверяет, является ли треугольник прямоугольным.

  Args:
      a: Длина первой стороны треугольника.
      b: Длина второй стороны треугольника.
      c: Длина третьей стороны треугольника.

  Returns:
      True, если треугольник прямоугольный, False - в противном случае.
  """
    return a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2
