#!/usr/bin/python
class Person:
  def __init__(self, fname, lname, age):
    self.fname = fname
    self.lname = lname
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.fname)

  def printname(self):
    print self.fname, self.lname

p1 = Person("John", "Rogers", 36)
p1.myfunc()

class Student(Person):
    def __init__(self, fname, lname, age, year):
      Person.__init__(self, fname, lname, age)
      self.graduationyear = year

x = Student("Mike", "Olsen", 28, 2019)
x.printname()
print x.graduationyear
