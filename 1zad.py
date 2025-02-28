class CustomList:
    def __init__(self, a):
        if a <= 0:
            raise ValueError("Размер списка должен быть положительным числом.")
        self._data = [0] * a
        self.n = a
        self.writes = 0
        self.reads = 0
    def get_counters(self):
        return {"writes": self.writes, "reads": self.reads}
    def getitem(self, idx):
        if 0 <= idx < self.n:
            self.reads += 1
            return self._data[idx]
        else:
            raise IndexError("Индекс выходит за границы списка.")
    def setitem(self, idx, val):
        if 0 <= idx < self.n:
            if -100 <= val <= 100:
                self._data[idx] = val
                self.writes += 1
            else:
                raise ValueError("Значение должно быть в диапазоне от -100 до 100.")
        else:
            raise IndexError("Индекс выходит за границы списка.")
    def display(self):
        """Выводит все значения списка."""
        print(self._data)