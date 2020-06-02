import time


class Median_filter:
    def __init__(self, __step: int):
        self.LINE = 0
        self.SIZE = 0
        self.STEP = __step
        self.__MASS = []
        self.__MATRIX = []
        self.MATRIX_NEW = []
        self.__BUFFER = []
        self.__aaa = 0
        self.__count = 0
        self.__size = 0

    @staticmethod
    def max_element(__a, __b):
        return __a if __a > __b else __b

    @staticmethod
    def min_element(__a, __b):
        return __a if __a < __b else __b

    def f_middle_element(self, __a, __b, __c):
        return self.max_element(self.max_element(self.min_element(__a, __b), self.min_element(__a, __c)),
                                self.min_element(__b, __c))

    def middle_of_3(self, cheak: int):
        __temp = 0
        if self.__aaa == 0:
            self.__MASS.append(cheak)
            return self.__MASS[self.__aaa]
        else:
            for i in range(self.__aaa):
                __temp = self.__MATRIX[i]
                self.__MASS.append(__temp[self.__size - 1])
            self.__MASS.append(cheak)
            __count = 0
            __aaa = 0
            self.__BUFFER = [0] * self.STEP
            for newVal in self.__MASS:
                self.__BUFFER[__count] = newVal
                if __aaa < 2:
                    if __aaa == 0:
                        __temp = newVal
                    elif __aaa == 1:
                        __temp = self.__BUFFER[__aaa] if self.__BUFFER[__aaa] >= self.__BUFFER[__aaa - 1] else \
                            self.__BUFFER[
                                __aaa - 1]
                else:
                    __temp = self.f_middle_element(self.__BUFFER[__count], self.__BUFFER[__count - 1],
                                                   self.__BUFFER[__count - 2])
                __aaa += 1
                __count += 1
                if __count >= self.STEP:
                    __count = 0
        return __temp

    def middle_more_than_3(self, cheak: int):
        __temp = 0
        if self.__aaa == 0:
            self.__MASS.append(cheak)
            return self.__MASS[self.__aaa]
        else:
            for i in range(self.__aaa):
                __temp = self.__MATRIX[i]
                self.__MASS.append(__temp[self.__size - 1])
            self.__MASS.append(cheak)
            __count = 0
            __aaa = 0
            self.__BUFFER = []
            for newVal in self.__MASS:
                if __aaa < self.STEP:
                    self.__BUFFER.append(newVal)
                    __temp_s = sorted(self.__BUFFER)
                    __temp = __temp_s[int((__aaa + 1) / 2)]
                else:
                    self.__BUFFER[__count] = newVal
                    __temp_s = sorted(self.__BUFFER)
                    __temp = __temp_s[int(self.STEP / 2)]
                __aaa += 1
                __count += 1
                if __count >= self.STEP:
                    __count = 0
        return __temp

    def update(self, line: list):
        self.__MATRIX.append(line)
        self.LINE = line
        self.SIZE = len(self.LINE)
        self.__size = 0
        __temp = []
        for n in self.LINE:
            self.__MASS = []
            self.__size += 1
            if self.STEP < 3:
                exit("\nLack of input")
            if self.STEP == 3:
                __temp.append(self.middle_of_3(n))
            else:
                __temp.append(self.middle_more_than_3(n))
        self.__aaa += 1
        self.__count += 1
        if self.__count >= self.STEP:
            self.__count = 0
        self.MATRIX_NEW.append(__temp)
        return __temp


fin = open('input.txt', "r")

all_files = fin.read().split()
ccc = []
for i in all_files:
    ccc.append(int(i))

a = [[10, 8, 30, 5],
     [8, 7, 40, 3],
     [11, 10, 20, -3],
     [10, 15, 50, 2],
     [12, -3, 30, 1]]
start_time = time.time()
balance = Median_filter(5)
for i in a:
    print(balance.update(i))
print((time.time() - start_time))
