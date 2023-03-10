

# class myclass:
#     x=5

# p=myclass
# print(p.x)

# class myclass:
#     def display(name, age, gender, rollno, div):
#         # return("Hello World")
#         print("Name : "+name)
#         print("Age : "+age)
#         print("Gender : "+gender)
#         print("Roll No : "+rollno)
#         print("Div : "+div)

# p=myclass
# p.display("Ayesha","19","Female","72","S14")

#use self when no parameters passed
# class myclass:
#     def display(self):
#         # return("Hello World")
#         print("Hello world")    
# p=myclass()
# p.display()

# single level
# class A():
#     def display():
#         print("A")

# class B(A):
#     def show():
#         print("B")

# obj = B
# obj.display()
# obj.show()

# multiple level
# class A():
#     def display():
#         print("A")

# class B(A):
#     def show():
#         print("B")


# class C(B):
#     def define():
#         print("C")

# obj = C
# obj.display()
# obj.show()
# obj.define()

# multilevel
# class A():
#     def display():
#         print("A")

# class B():
#     def show():
#         print("B")


# class C(B,A):
#     def define():
#         print("C")

# obj = C
# obj.display()
# obj.show()
# obj.define()

class A():
    def display():
        print("A")

class B(A):
    def show():
        print("B")

class C(A):
    def define():
        print("C")



obj = B
obj2=C
obj.display()
obj.show()
obj2.display()
obj2.define()
