import time


class Median_filter:
    def __init__(self, __step: int, __amount=1):
        self.STEP = __step
        self.AMOUNT = __amount
        self.MASS = []
        self.BUFFER = [0] * self.STEP
        self.LINE = 0
        self.__aaa = 0
        self.__count = 0

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

        cheak = self.LINE
        # if self.MASS:
        #     cheak = self.MASS
        # else:
        #     self.MASS = [0] * self.SIZE
        self.BUFFER[self.__count] = cheak
        if self.__aaa < 2:
            if self.__aaa == 0:
                self.MASS.append(cheak)
            elif self.__aaa == 1:
                self.MASS.append(
                    self.BUFFER[self.__aaa] if self.BUFFER[self.__aaa] >= self.BUFFER[self.__aaa - 1] else self.BUFFER[
                        self.__aaa - 1])
        else:
            self.MASS.append(
                self.f_middle_element(self.BUFFER[self.__count], self.BUFFER[self.__count - 1],
                                      self.BUFFER[self.__count - 2]))
        self.__aaa += 1
        self.__count += 1
        if self.__count >= self.STEP:
            self.__count = 0
        return self.MASS[self.__aaa - 1]

    def middle_more_than_3(self):
        cheak = self.LINE

        if self.__aaa < self.STEP:
            self.BUFFER[self.__count] = cheak
            __temp = []
            for i in range(0, self.__aaa + 1):
                __temp.append(self.BUFFER[i])
            self.MASS.append(__temp[int((self.__aaa + 1) / 2)])
        else:
            self.BUFFER[self.__count] = cheak
            __temp = sorted(self.BUFFER)
            self.MASS.append(__temp[int(self.STEP / 2)])
        self.__aaa += 1
        self.__count += 1
        if self.__count >= self.STEP:
            self.__count = 0
        return self.MASS[self.__aaa - 1]

    def update(self, line: int):
        self.LINE = line
        for i in range(self.AMOUNT):
            if self.STEP < 3:
                exit("\nLack of input")
            if self.STEP == 3:
                return self.middle_of_3()
            else:
                return self.middle_more_than_3()


fin = open('input.txt', "r")

all_files = fin.read().split()
ccc = []
for i in all_files:
    ccc.append(int(i))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
balance = Median_filter(3)
for i in a:
    print(balance.update(i))
