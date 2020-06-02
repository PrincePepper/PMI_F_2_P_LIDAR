import time
import sys  # sys нужен для передачи argv в QApplication


class Median_filter:
    def __init__(self, line: list, __step: int, __amount: int):
        self.LINE = line
        self.SIZE = len(line)
        self.STEP = __step
        self.AMOUNT = __amount
        self.MASS = []

    @staticmethod
    def max_element(__a, __b):
        return __a if __a > __b else __b

    @staticmethod
    def min_element(__a, __b):
        return __a if __a < __b else __b

    def f_middle_element(self, __a, __b, __c):
        return self.max_element(self.max_element(self.min_element(__a, __b), self.min_element(__a, __c)),
                                self.min_element(__b, __c))

    def middle_of_3(self):
        __count = 0
        __aaa = 0
        cheak = self.LINE
        if self.MASS:
            cheak = self.MASS
        else:
            self.MASS = [0] * self.SIZE
        buffer = [0] * self.STEP
        for newVal in cheak:
            buffer[__count] = newVal
            if __aaa < 2:
                if __aaa == 0:
                    self.MASS[__aaa] = newVal
                elif __aaa == 1:
                    self.MASS[__aaa] = buffer[__aaa] if buffer[__aaa] >= buffer[__aaa - 1] else buffer[__aaa - 1]

            else:
                self.MASS[__aaa] = self.f_middle_element(buffer[__count], buffer[__count - 1], buffer[__count - 2])
            __aaa += 1
            __count += 1
            if __count >= self.STEP:
                __count = 0

    def middle_more_than_3(self):
        __count = 0
        __aaa = 0
        cheak = self.LINE
        if self.MASS:
            cheak = self.MASS
        else:
            self.MASS = [0] * self.SIZE
        buffer = []
        for newVal in cheak:
            if __aaa < self.STEP:
                buffer.append(newVal)
                __temp = sorted(buffer)
                self.MASS[__aaa] = __temp[int(__aaa / 2)]
            else:
                buffer[__count] = newVal
                __temp = sorted(buffer)
                self.MASS[__aaa] = __temp[int(self.STEP / 2)]
            __aaa += 1
            __count += 1
            if __count >= self.STEP:
                __count = 0

    def start(self):
        for i in range(self.AMOUNT):
            if self.STEP < 3:
                exit("\nLack of input")
            if self.STEP == 3:
                self.middle_of_3()
            else:
                self.middle_more_than_3()
            return self.MASS


fin = open('input.txt', "r")

all_files = fin.read().split()
ccc = []
for i in all_files:
    ccc.append(int(i))
# a = [20, 29, 45, 53, 7, 81]
start_time = time.time()
balance = Median_filter(ccc, 3, 1)
bbb = balance.start()
print((time.time() - start_time))
