class Median_filter:
    def __init__(self, _step: int, position=False):
        self._matrix = []  # Список всех входных строк
        self.step = _step  # Шаг медианного фильтра
        self.position = position  # Определяет что выводить при четном шаге медианного фильтра

    @staticmethod
    def average_of_2(_a: int, _b: int):  # Вычисляет среднее арифметическое среди 2-х элементов
        return int((_a + _b) / 2)

    def middle_more_than_3(self, _column: int):  # Вычисляет медианный элемент при шаге > 3
        _temp = 0
        _count = 0
        _buffer = []
        for newVal in self._matrix:
            if _count < self.step:
                _buffer.append(newVal[_column])
                _temp_s = sorted(_buffer)
                if (_count + 1) % 2 == 0 and self.position:
                    _temp = self.average_of_2(_temp_s[int(_count / 2)], _temp_s[int((_count + 1) / 2)])
                else:
                    _temp = _temp_s[int((_count + 1) / 2)]
            else:
                _buffer[_count % self.step] = newVal[_column]
                if self.step % 2 == 0 and self.position:
                    _temp = self.average_of_2(_buffer[int(self.step / 2)], _buffer[int((self.step - 1) / 2)])
                else:
                    _temp = sorted(_buffer)[int(self.step / 2)]
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
                _temp.append(self.middle_more_than_3(_column))
        return _temp  # Возвращает готовую последовательнсть в зависимости от вх. данных


fin = open('input.txt', "r")
all_files = fin.read().split("\n")

a = [[10, 8, 30, 5],
     [8, 7, 40, 3],
     [11, 10, 20, -3],
     [10, 15, 50, 2],
     [12, -3, 30, 1]]
balance = Median_filter(6)
for i in a:
    print(balance.update(i))

# результат при step(d) = 5
# [10, 8, 30, 5]
# [10, 8, 40, 5]
# [10, 8, 30, 3]
# [10, 10, 40, 3]
# [10, 8, 30, 2]
