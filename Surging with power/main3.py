def power(x,y):
    result = 1
    for i in range(abs(y)):
       result = result * x
    if y < 0:
        return 1/ result
    else:
        return result
x=float(input("Enter the base (x): "))
y=int(input("Enter the exponent (y): "))
print(f"{x} to the power of{y} is: {power(x, y)} ")
    