import random

class Median_filter:
    def __init__(self, _step: int, position=False):
        self._matrix = []  # Список всех входных строк
        self.step = _step  # Шаг медианного фильтра
        self.position = position  # Определяет что выводить при четном шаге медианного фильтра

    def quickselect_median(self, l, pivot_fn=random.choice):
        if self.position and len(l) % 2 == 0:
            return 0.5 * (self.quickselect(l, int(len(l) / 2) - 1, pivot_fn) +
                          self.quickselect(l, int(len(l) / 2), pivot_fn))
        else:
            return self.quickselect(l, int(len(l) / 2), pivot_fn)

    def quickselect(self, l, k, pivot_fn):
        """
        Выбираем k-тый элемент в списке l (с нулевой базой)
        :param l: список числовых данных
        :param k: индекс
        :param pivot_fn: функция выбора pivot, по умолчанию выбирает случайно
        :return: k-тый элемент l
        """
        if len(l) == 1:
            assert k == 0
            return l[0]

        pivot = pivot_fn(l)

        lows = [el for el in l if el < pivot]
        highs = [el for el in l if el > pivot]
        pivots = [el for el in l if el == pivot]

        if k < len(lows):
            return self.quickselect(lows, k, pivot_fn)
        elif k < len(lows) + len(pivots):
            # Нам повезло и мы угадали медиану
            return pivots[0]
        else:
            return self.quickselect(highs, k - len(lows) - len(pivots), pivot_fn)

    def middle_value(self, _column: int):
        _temp = 0
        _count = 0
        _buffer = []
        for newVal in self._matrix:
            if _count < self.step:
                _buffer.append(newVal[_column])
                _temp = self.quickselect_median(_buffer)
            else:
                _buffer[_count % self.step] = newVal[_column]
                _temp = self.quickselect_median(_buffer)
            _count += 1
        return _temp

    def update(self, line: list):
        if self.step == 1:  # Возвращает последовательность какая она и была
            return line
        self._matrix.append(line)
        _temp = []
        for _column, n in enumerate(line):
            if len(self._matrix) == 1:  # Проверка на первую входную последовательность
                _temp.append(n)
            else:
                _temp.append(self.middle_value(_column))
        return _temp  # Возвращает готовую последовательнсть в зависимости от вх. данных


"""
    2 способа ввода:
    - через файл
    - через список
    
    Если хочешь через файл, следует удалить:
     a = [[10, 8, 30, 5],
          [8, 7, 40, 3],
          [11, 10, 20, -3],
          [10, 15, 50, 2],
          [12, -3, 30, 1]]
"""
lines = [line.rstrip('\n') for line in open('input.txt')]
a = []
for i in lines:
    a.append([int(j) for j in i.split()])

a = [[10, 8, 30, 5],
     [8, 7, 40, 3],
     [11, 10, 20, -3],
     [10, 15, 50, 2],
     [12, -3, 30, 1]]

balance = Median_filter(5)
for i in a:
    print(balance.update(i))