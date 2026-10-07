class Student:
        brand = "Liya"
        addres = "Bang"
        owner = "liya"
        phno = 50
        amount = 10.5
        arr = None
        arr1 = ""

        def brandis(self):
            print("Brand name is :",self.brand)
            print(type(self.brand))
            print(type(self.phno))
            print(type(self.amount))
            print(type(self.arr))
            print(self.arr)
            
        def add(self):
            print("Address : ", self.addres)
            # print(len(self.arr))
            print(len(self.arr1))

ref = Student()
ref.brandis()
ref.add()
ref2 = ref
ref2.add()
ref3 = ref2
print(ref3.brand)
