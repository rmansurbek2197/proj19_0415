# 11-masala
class Dog:
    def speak(self):
        return "Woof"

print("11:", Dog().speak())


# 12-masala
class Math:
    def square(self, x):
        return x*x

print("12:", Math().square(6))


# 13-masala
class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello {self.name}"

print("13:", User("Ali").greet())


# 14-masala
class Laptop:
    def __init__(self, price):
        self.price = price

    def discount(self):
        return self.price * 0.9

print("14:", Laptop(1000).discount())


# 15-masala
class Timer:
    def __init__(self):
        self.t = 0

    def tick(self):
        self.t += 1

tm = Timer()
tm.tick()
tm.tick()
print("15:", tm.t)
