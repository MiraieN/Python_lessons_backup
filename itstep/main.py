# def simpleDecorator(myFunction):
#     print("Hello! I'm Decorator1!")
#     def simpleWrapper():
#         print("Function starts working...1")
#         myFunction()
#         print("See you!1")
#     print("1")
#     return simpleWrapper

# def simpleDecorator_v2(myFunction):
#     print("Hello! I'm Second Decorator2!")
#     def simpleWrapper():
#         print("Let's start...2")
#         myFunction()
#         print("Good luck!2")
#     print("2")
#     return simpleWrapper

# @simpleDecorator
# @simpleDecorator_v2
# def sayHi():
#     print("Welcome!")
# sayHi()


# def teeth_cure(symptoms, time, money):
#     print("Telling doctor the symptoms")
#     print("Setting on time")
#     print("Coming to the doctor at the set time")
#     print("Waiting...")
#     print("Giving the money")
#     return "No more teeth pain"   


# teeth_pain = True
# if teeth_pain:
#     teeth_cure("pain in teeth", "13:30", "$50")
#     teeth_pain = False

# import math
# x=0.23
# y=1.87
# z=3
# print(math.ceil(x)) #1
# print(math.ceil(y)) #2
# print(math.ceil(z)) #3
# print(math.floor(x)) #0
# print(math.floor(y)) #1
# print(math.floor(z)) #3

# def func():
#     global a
#     a = 4
# a = 5
# func()
# print(a)

# def func():
#     print(a)

# a = 5
# func()

def func_1():
    global func_2
    def func_2():
        print("2")
        return 1
    print("1")
func_1().func_2()
