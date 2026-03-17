from threading import Condition

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.i = 1
        self.cv = Condition()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz):
        while True:
            with self.cv:
                while self.i <= self.n and not (self.i % 3 == 0 and self.i % 5 != 0):
                    self.cv.wait()
                
                if self.i > self.n:
                    self.cv.notify_all()
                    return
                
                printFizz()
                self.i += 1
                self.cv.notify_all()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz):
        while True:
            with self.cv:
                while self.i <= self.n and not (self.i % 5 == 0 and self.i % 3 != 0):
                    self.cv.wait()
                
                if self.i > self.n:
                    self.cv.notify_all()
                    return
                
                printBuzz()
                self.i += 1
                self.cv.notify_all()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz):
        while True:
            with self.cv:
                while self.i <= self.n and not (self.i % 15 == 0):
                    self.cv.wait()
                
                if self.i > self.n:
                    self.cv.notify_all()
                    return
                
                printFizzBuzz()
                self.i += 1
                self.cv.notify_all()

    # printNumber(x) outputs "x"
    def number(self, printNumber):
        while True:
            with self.cv:
                while self.i <= self.n and not (self.i % 3 != 0 and self.i % 5 != 0):
                    self.cv.wait()
                
                if self.i > self.n:
                    self.cv.notify_all()
                    return
                
                printNumber(self.i)
                self.i += 1
                self.cv.notify_all()