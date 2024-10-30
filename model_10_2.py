import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power, enemies=0, day=0):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies = enemies
        self.day = day

    def time(self):
        self.enemies = 100
        while self.enemies > 0:
            self.day += 1
            time.sleep(1)
            if self.enemies - self.power > 0:
                self.enemies -= self.power
                print(f'{self.name} сражается {self.day} дней, осталось {self.enemies} воинов')
            else:
                break

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.time()
        print(f'{self.name} одержал победу спустя {self.day} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
