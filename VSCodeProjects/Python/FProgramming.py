from functools import partial
import functools

# compostition: function as parameter 
def f(x):
    return x + 2

def g(h, x):
    return h(x) * 2

print(g(f,42))




#Closure: function as result/return 
# x: captured variable y: free variable
def addx(x):
    def _(y):
        return x+y
    return _

add2 = addx(2)
add3 = addx(3)
print(add2,add3) #function address
print(add2(2),add3(3)) #function values




#Currying: get function with many arguments and reduce it to one argument
def f(x,y):
    return x*y

def f2(x):
    def _(y):
        return f(x,y)
    return _

print(f2(2)) #function address
print(f2(2)(3)) #function values

#partial function: similar to currying
def multiply(x,y):
    return x * y
# create a new function that multiplies by 2
func = partial(multiply,2) 
print(func(4))
