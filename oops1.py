class Fan:
    def __init__(self):
        self.brand = "Bajaj"
        self.color = "Black"
        self.cost =  3000
        self.noOfBlades = 3
    def on(self):
        print("Fan is On")
        print(self.color)
        print(self.brand)
        print(self.cost)
        print(self.noOfBlades)
    def rotate(self):
        print("Fan is rotating")
    def off(self):
        print("Fan is off")
f1 = Fan()
f1.on()
f1.rotate()
f1.off()
