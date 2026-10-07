# no para and return valuw

class Demo:
    def __init__(self):
        self.a = 10
        self.b = 20

    def disp(self):
        x = 100
        y = 200
        z = x+y
        return z
d1 = Demo()
print(d1.a)
print(d1.b)
n = d1.disp()
print(n)