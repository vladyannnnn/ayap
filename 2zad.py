class CustomList:
    def __init__(self, n):
        if n <= 0:
            raise ValueError("Размер списка должен быть положительным числом.")
        self._a = [0] * n
        self.b = n
        self.c = 0
        self.d = 0
    def get_counters(self):
        return {"c": self.c, "d": self.d}
    def getitem(self, i):
        if 0 <= i < self.b:
            self.d += 1
            return self._a[i]
        else:
            raise IndexError("Индекс выходит за границы списка.")
    def setitem(self, i, v):
        if 0 <= i < self.b:
            if -100 <= v <= 100:
                self._a[i] = v
                self.c += 1
            else:
                raise ValueError("Значение должно быть в диапазоне от -100 до 100.")
        else:
            raise IndexError("Индекс выходит за границы списка.")
    def append(self, v):
        if -100 <= v <= 100:
            self._a.append(v)
            self.b += 1
            self.c += 1
        else:
            raise ValueError("Значение должно быть в диапазоне от -100 до 100.")
    def display(self):
        """Выводит все значения списка."""
        print(self._a)