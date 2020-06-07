class Median_filter:
    def __init__(self, _step: int):
        self._matrix = []                                           # Список всех входных строк
        self.step = _step                                           # Шаг медианного фильтра
        self._buffer = [0] * self.step                              # Массив длинной шага медианного фильтра
        self._size = 0                                              # Отвечает за проход по столбцам

    @staticmethod
    def f_middle_element(_a, _b, _c):                               # Вычисляет средний элемент среди 3-х
        return max(max(min(_a, _b), min(_a, _c)), min(_b, _c))

    def average_of_2(self):                                         # Вычисляет среднее арифметическое среди 2-х элементов
        _aaa = self._matrix[len(self._matrix) - 1][self._size]
        _bbb = self._matrix[len(self._matrix) - 2][self._size]
        return (_aaa + _bbb) / 2

    def middle_of_3(self):                                          # Вычисляет медианный элемент при шаге = 3
        pos = True
        _temp = 0
        _count = 0
        for newVal in self._matrix:
            self._buffer[_count] = newVal[self._size]
            if _count < self.step and pos:
                if _count == 0:
                    _temp = newVal[self._size]
                elif _count == 1:
                    _temp = self._buffer[1] if self._buffer[1] >= self._buffer[0] else self._buffer[0]
                    pos = False
            else:
                _temp = self.f_middle_element(self._buffer[0], self._buffer[1], self._buffer[2])
            _count += 1
            if _count == self.step:
                _count = 0
        return _temp

    def middle_more_than_3(self):                                   # Вычисляет медианный элемент при шаге > 3
        pos = True
        _temp = 0
        _count = 0
        _aaa = []
        for newVal in self._matrix:
            self._buffer[_count] = newVal[self._size]
            if _count < self.step and pos:
                _aaa.append(newVal[self._size])
                _temp_s = sorted(_aaa)
                _temp = _temp_s[int((_count + 1) / 2)]
                if _count + 1 == self.step:
                    pos = False
            else:
                _temp = sorted(self._buffer)[int(self.step / 2)]
            _count += 1
            if _count >= self.step:
                _count = 0
        return _temp

    def update(self, line: list):
        if self.step == 1:                                          # Возвращает последовательность какая она и была
            return line
        self._matrix.append(line)
        self._size = 0
        _temp = []
        for n in line:
            if len(self._matrix) == 1:                              # Проверка на первую входную последовательность
                _temp.append(n)
            elif self.step == 2:
                _temp.append(self.average_of_2())
            elif self.step == 3:
                _temp.append(self.middle_of_3())
            else:
                _temp.append(self.middle_more_than_3())
            self._size += 1
        return _temp                                                # Возвращает готовую последовательнсть в зависимости от вх. данных


fin = open('input.txt', "r")
all_files = fin.read().split("\n")

a = [[10, 8, 30, 5],
     [8, 7, 40, 3],
     [11, 10, 20, -3],
     [10, 15, 50, 2],
     [12, -3, 30, 1]]
balance = Median_filter(3)
for i in a:
    print(balance.update(i))

# результат при step(d) = 5
# [10, 8, 30, 5]
# [10, 8, 40, 5]
# [10, 8, 30, 3]
# [10, 10, 40, 3]
# [10, 8, 30, 2]
