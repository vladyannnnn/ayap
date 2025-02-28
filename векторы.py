class Vector:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.dx = x2 - x1
        self.dy = y2 - y1

    def __add__(self, other):
        return Vector(0, 0, self.dx + other.dx, self.dy + other.dy)

    def __str__(self):
        return f"Вектор: ({self.dx}, {self.dy})"


x1, y1, x2, y2 = map(float, input("Введите координаты начала и конца первого вектора (x1, y1, x2, y2): ").split())
x3, y3, x4, y4 = map(float, input("Введите координаты начала и конца второго вектора (x3, y3, x4, y4): ").split())

vector1 = Vector(x1, y1, x2, y2)
vector2 = Vector(x3, y3, x4, y4)
vector_sum = vector1 + vector2

print("Сумма векторов:", vector_sum)