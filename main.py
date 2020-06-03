import time


class Median_filter:
    def __init__(self, _step: int):
        self._matrix = []
        self._mass = []
        self._buffer = []
        self.step = _step
        self._selfaccess = 0
        self._count = 0
        self._size = 0

    @staticmethod
    def f_middle_element(_a, _b, _c):
        return max(max(min(_a, _b), min(_a, _c)), min(_b, _c))

    def middle_of_3(self, cheak: int):
        _temp = 0
        _count = 0
        if self._selfaccess == 0:
            self._mass.append(cheak)
            return self._mass[self._selfaccess]
        else:
            for i in range(self._selfaccess):
                _temp = self._matrix[i]
                self._mass.append(_temp[self._size - 1])
            self._mass.append(cheak)
            self._buffer = []
            for newVal in self._mass:
                if len(self._buffer) < 3:
                    self._buffer.append(newVal)
                    if _count == 0:
                        _temp = newVal
                    if _count == 1:
                        _temp = self._buffer[1] if self._buffer[1] >= self._buffer[0] else self._buffer[0]
                else:
                    self._buffer[_count] = newVal
                    _temp = self.f_middle_element(self._buffer[0], self._buffer[1], self._buffer[2])
                _count += 1
                if _count == self.step:
                    _count = 0
        return _temp

    def middle_more_than_3(self, cheak: int):
        _temp = 0
        _count = 0
        if self._selfaccess == 0:
            self._mass.append(cheak)
            return self._mass[self._selfaccess]
        else:
            for i in range(self._selfaccess):
                _temp = self._matrix[i]
                self._mass.append(_temp[self._size - 1])
            self._mass.append(cheak)
            self._buffer = []
            for newVal in self._mass:
                if len(self._buffer) < self.step:
                    self._buffer.append(newVal)
                    _temp_s = sorted(self._buffer)
                    _temp = _temp_s[int((_count + 1) / 2)]
                if len(self._buffer) == self.step:
                    self._buffer[_count] = newVal
                    _temp_s = sorted(self._buffer)
                    _temp = _temp_s[int((self.step + 1) / 2)]
                _count += 1
                if _count >= self.step:
                    _count = 0
        return _temp

    def update(self, line: list):
        if self.step == 1:
            return line
        self._matrix.append(line)
        self._size = 0
        _temp = []
        for n in line:
            self._mass = []
            self._size += 1
            if self.step == 2:
                pass
            elif self.step == 3:
                _temp.append(self.middle_of_3(n))
            else:
                _temp.append(self.middle_more_than_3(n))

        self._selfaccess += 1
        self._count += 1
        if self._count >= self.step:
            self._count = 0
        return _temp


fin = open('input.txt', "r")
all_files = fin.read().split()
ccc = []
for i in all_files:
    ccc.append(int(i))

a = [[10, 8, 30, 5],
     [10, 8, 40, 5],
     [10, 8, 40, 5],
     [10, 10, 40, 2],
     [11, 10, 30, 1]]
start_time = time.time()
balance = Median_filter(1)
for i in a:
    print(balance.update(i))
print((time.time() - start_time))
