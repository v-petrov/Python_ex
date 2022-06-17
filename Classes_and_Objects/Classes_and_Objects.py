# class MyClass:
#     variable = "blah"

#     def function(self):
#         print("This is a message inside the class")
    
# myobjectx = MyClass()
# myobjecty = MyClass()

# myobjecty.variable = "yackity"

# print(myobjectx.variable)
# print(myobjecty.variable)

# print(myobjectx.function())

# class Vehicle:
#     name = ""
#     kind = ""
#     color = ""
#     value = 0.00
#     def description(self):
#         desc_str = "%s is a %s %s worth $%.2f" % (self.name, self.color, self.kind, self.value)
#         return desc_str

# car1 = Vehicle()
# car1.name = "Fer"
# car1.kind = "convertible"
# car1.color = "red"
# car1.value = 60000.00

# car2 = Vehicle()
# car2.name = "Jump"
# car2.kind = "van"
# car2.color = "blue"
# car2.value = 10000.00

# print(car1.description())
# print(car2.description())

# ----------------------------------------

# class MyClass:
#     i = 1234

#     def __init__(self,data): # constructor с параметър, инстанция
#         self.dat = data

#     def add_data(self,data):
#         self.dat.append(data)
#     def f(self):
#         return 'Hello, OOP!'

# print(MyClass.i,MyClass.f)
# # x = MyClass() #Constructor
# x = MyClass([1,2,3,4,5])
# print(x.f(), x.f)
# print(x.dat, x.i)
# y = MyClass(['a','b','c'])
# print(y.dat, y.i)
# y.add_data([1,2,3])
# print(y.dat)
#------------------------------------------------------------

class Student:
    def __init__(self, fnum, name, mark):
        self.fnum = fnum
        self.name = name
        self.mark = mark

    def __str__(self):
        return 'Student('+str(self.fnum)+', '+self.name+', '+str(self.mark)+')'


class StudentGroup:
    def __init__(self):
        self.group = []

    def add_student(self, student):
        self.group.append(student)

    def remove_student(self, student):
        self.group.remove(student)

    def average_mark(self):
        sum = 0
        for student in self.group:
            sum += student.mark
        return round(sum/len(self.group), 2)

    def minimum_mark(self):
        min = self.group[0]
        for student in self.group:
            if min.mark > student.mark:
                min = student
        return min

    def maximum_mark(self):
        max = self.group[0]
        for student in self.group:
            if max.mark < student.mark:
                max = student
        return max

    def sort(self):
        for i in range(len(self.group)):
            min = i
            for j in range(i+1, len(self.group)):
                if self.group[min].mark > self.group[j].mark:
                    min = j
            temp = self.group[i]
            self.group[i] = self.group[min]
            self.group[min] = temp

    def __str__(self):
        out = ''
        for student in self.group:
            out += str(student)+'\n'
        return out
        # return str([str(student) for student in self.group])


# fnum = int(input('FNo:'))
# name = input('Name:')
# mark = float(input('Mark:'))
# st1 = Student(fnum, name, mark)
# print(st1.__str__())
# print(st1)
# print(st1.__repr__())

st1 = Student(123, 'Ivan', 5.66)
# st2 = Student(122, 'Petyr', 5.32)
# st3 = Student(223, 'Dimityr', 5.44)
# st4 = Student(222, 'Lili', 5.21)
# st5 = Student(323, 'Georgi', 5.11)
# st6 = Student(322, 'Maria', 5.13)
print(st1)
# print(st2)
# print(st3)
# print(st4)
# print(st5)
# print(st6)
# group = StudentGroup()

# print(group)
# group.add_student(st1)
# print(group)
# group.add_student(st2)
# print(group)
# group.add_student(st3)
# group.add_student(st4)
# group.add_student(st5)
# group.add_student(st6)
# print(group)
# print(group.average_mark())
# print(group.minimum_mark())
# print(group.maximum_mark())
# group.sort()
# print(group)

#--------------------------------------------
import math

class Shape:
    def __init__(self, number):
        self.sides = [0 for x in range(number)]
        self.n = number

    def input_sides(self):
        self.sides = [float(input('Side ' + str(i + 1) + ': ')) for i in range(self.n)]
    
    def display_sides(self):
        print(self.sides)
    
    def get_perimeter(self):
        return sum(self.sides)

class Triangle(Shape):
    def __init__(self):
        super().__init__(3)

    def get_area(self):
        p = self.get_perimeter() / 2
        a,b,c = self.sides
        s = math.sqrt(p*(p-a)*(p-b)*(p-c))
        return s

class Rectangle(Shape):
    def __init__(self):
        Shape.__init__(self, 2)

# overriding => virtual methods
    def get_perimeter(self):
        return super().get_perimeter() * 2

    def get_area(self):
        a,b = self.sides
        s = a * b
        return s

t = Triangle()
t.display_sides()
t.input_sides()
t.display_sides()
print(t.get_perimeter())
print(t.get_area())

r = Rectangle()
r.display_sides()
r.input_sides()
r.display_sides()
print(r.get_perimeter())
print(r.get_area())

# print(isinstance(t, Rectangle))
# print(isinstance(t, Triangle))
# print(isinstance(r, Rectangle))
# print(isinstance(r, Triangle))
# print(isinstance(t, Shape))
# print(isinstance(r, Shape))
# print(10*'=')
# print(issubclass(Triangle, Shape))
# print(issubclass(Rectangle, Shape))

# class Reverse:
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index -= 1
#         return self.data[self.index]


# rev = Reverse([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(rev)

# li1 = [x for x in Reverse([1,2,3,4,5,6,7,8,9])]
# print(li1)

list1 = [1,2,3,4,5,6]
list2 = list1.copy()
# del list2[:]
# print(list2)
for x in range(len(list2)-1, -1, -1):
    del list2[x]
print(list2)

for x in range(len(list1)-1, -1, -1):
    list2.append(list1[x])
print(list2)

# def reverse(l):
#     for index in range(len(l)-1, -1, -1):
#         yield l[index]

# l1 = [x for x in reverse([1,2,3,4,5,6,7,8,9,10,11])]
# print(l1)

# xlist = [10, 20, 30]
# ylist = [7, 5, 3]
# print(sum(x*y for x,y in zip(xlist,ylist)))
# print(sum(x*x for x in xlist))

# import random
# letters = 'qazwsxedcrfvtgbyhnujmikolp'
# letters_in_caps = 'QAZWSXEDCRFVTGBYHNUJMIKOLP'
# digits = '0123456789'
# simbols = '`!/.,][}=-{'
# password = ''

# all = letters + letters_in_caps + digits + simbols

# for x in range(10):
#         for element in random.choice(all):
#                 password += element
# print(f'Your password is: {password}')

# def str1(word):
#         return f'{word} :)'
# str_1 = str1('Hi')
# print(str_1)