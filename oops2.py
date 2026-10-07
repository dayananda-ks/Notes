class Student:
    def __init__(self):
        self.brand = "Liya"
        self.addres = "Bang"
        self.owner = "liya"

    def brandis(self):
        print("Brand name is :",self.brand)
    def add(self):
        print("Address : ", self.addres)

ref = Student()
ref.brandis()
ref.add()
ref2 = ref
ref2.add()
ref3 = ref2
print(ref3.brand)
