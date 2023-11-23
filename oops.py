# class Car:
    
#     company = 'B M W'
#     def __init__(self,mod,mil,gear):
        
#         print('it shows all the car details')
        
#         self.mod = mod
#         self.mil = mil
#         self.gear = gear
        
#     def speed_limit(self):
#         self.speed = '250kmph'
#         print(self.speed)
    
    
# c1 = Car('a1',8,6)
# c1.speed_limit()

# class Bike:
    
#     def __init__(self):
#         self.gear = 'automatic'
#         self.gears = 6
#         self.mil = '35kmph'
        
#     def details(self):
#         print(self.gear)
#         print(self.gears)
#         print(self.mil)
        
# b1 = Bike()
# b2 = Bike()
# print(b1.gear)

# b2.gears = 5

# print(b2.details())


# class LCU:
#     def __init__ (self,hero_name,genre, release_year):
#         self.hero_name = hero_name
#         self.genre = genre
#         self.release_year = release_year
        
# kaidhi = LCU('Karthi','Action',2019)
# vikram = LCU('Kamal Hassan','Mystrey',2022)
# leo = LCU('Vijay','Gangstar','2023')


# print(kaidhi.hero_name,kaidhi.genre,kaidhi.release_year)
# print(vikram.hero_name,vikram.genre,vikram.release_year)
# print(leo.hero_name,leo.genre,leo.release_year)

# class LCU:
#     def __init__ (self,movie_name,hero_name,genre, release_year):
#         self.movie_name = movie_name
#         self.hero_name = hero_name
#         self.genre = genre
#         self.release_year = release_year
        
#     def movie(self):
#         print(self.movie_name)
#         print(self.hero_name)
#         print(self.genre)
#         print(self.release_year)
        
# movies = [LCU('Kaidhi','Karthi','Action',2019),LCU('Vikram','Kamal Hassan','Mystrey',2022),LCU('Leo','Vijay','Gangstar','2023')]

# for i in movies:
#     i.movie()


# class Emp:
    
#     org = 'Marolix tech.'
    
#     def __init__(self):
#         self.a = 10
#         self.b = 20
#     def add(self):
#         self.c = 30
        
# e1 = Emp()
# e2 = Emp()
# e2.org = 'Rubber'
# print(e1.__dict__)
# print(e2.__dict__)
# e1.add()
# print(e1.__dict__)
# # e2.add()
# # print(e2.__dict__)
# e2.c=40
# e2.add()
# e2.d=50
# print(e2.__dict__)

# print(e1.org)
# Emp.org = 'Plastic'
# print(e1.org)
# print(e2.org)

class Test:
    a=10
    def __init__(self):
        self.b = 20
    def m1(self):
        self.c=30
        print(self.c)
    @classmethod
    def cls_met(cls):
        cls.d=50
        Test.e=60
        print(cls.d)
        print(Test.e)
    @staticmethod
    def stat_met():
        Test.f = 15
        Test.e=45
        print('This is static method', Test.f)
        
t1 = Test()

t2 = Test()

# print(Test.a)

print(Test.__dict__)
print(t1.__dict__)
t1.m1()
t1.cls_met()
t1.stat_met()
print(Test.__dict__)
print(t1.__dict__)


















# print('t1:', t1.x, t1.y)
# print('t2:', t2.x, t2.y)

# t1.x=15
# Test.x=30
# t2.x=25
# print('t1:', t1.x, t1.y)
# print('t2:', t2.x, t2.y)
# print(Test.x)

# t1.cls_met()


