#with keyword:
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
myFun(firstname='swetha', lastname='A', age='20')

#Swithout keyword:

def myFun(*argv):
    for arg in argv:
        print(arg)
myFun('Hello', 'World', 'Im', 'swetha')