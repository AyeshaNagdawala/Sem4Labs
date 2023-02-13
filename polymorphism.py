# METHOD OVERLOADING

class addition :
    def add(self,a=None,b=None,c=None):
        if a is not None and b is not None and c is not None :
            print(a+b+c)

        elif a is not None and b is not None :
            print(a+b)

        else :
            print(a)
obj1=addition()
obj2=addition()
obj3=addition()
obj1.add(1,2,3)
obj2.add(1,2)
obj3.add(1)

# METHOD OVERRIDING

class A:
    def display(self):
        print("I am in A")

class B(A):
    def display(self):
        print("I am in B")
obj1=B()
obj1.display()
obj2=A()
obj2.display()
