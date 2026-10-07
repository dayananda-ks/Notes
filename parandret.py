# parameter and no return
class Demo:
    def __init__(self):
        self.a = 10
        self.b = 20

    def disp(self,name):
        return name
d1 = Demo()
k = d1.disp("daya")
print(k)
