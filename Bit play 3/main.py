#program to swap 2 numbers without a 3rd variable
def swap1(a,b):
    a=a^b
    b=a^b
    a=a^b
    print("After swapping: a =",a,"b=",b)
def swap2(a,b):
    a=(a&b)+(a|b)
    b=a+(~b)+1
    a=a+(~b+1)
    a=a+(~b)+1
    print("After swapping: a= ",a,"b=",b)
swap1(5,8)
swap2(10,45)