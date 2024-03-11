from geometry import circle_area, triangle_area, is_right_triangle

# Вычисление площади круга
radius = 5
circle_area = circle_area(radius)
print(f"Площадь круга с радиусом {radius}: {circle_area}")

# Вычисление площади треугольника
a = 3
b = 4
c = 5
triangle_area = triangle_area(a, b, c)
print(f"Площадь треугольника со сторонами {a}, {b}, {c}: {triangle_area}")

# Проверка, является ли треугольник прямоугольным
is_right = is_right_triangle(a, b, c)
print(f"Треугольник со сторонами {a}, {b}, {c} {'является' if is_right else 'не является'} прямоугольным")