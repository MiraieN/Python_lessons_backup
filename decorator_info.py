def simpleDecorator(myFunction):
    print("Hello! I'm Decorator1!")
    def simpleWrapper():
        print("Function starts working...1")
        myFunction()
        print("See you!1")
    print("1")
    return simpleWrapper

def simpleDecorator_v2(myFunction):
    print("Hello! I'm Second Decorator2!")
    def simpleWrapper():
        print("Let's start...2")
        myFunction()
        print("Good luck!2")
    print("2")
    return simpleWrapper

@simpleDecorator
@simpleDecorator_v2
def sayHi():
    print("Welcome!")
sayHi()
