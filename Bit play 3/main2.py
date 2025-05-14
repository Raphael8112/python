def divide(dividend,divisor):
    #check if the divisor is -ve or +ve
    sign=(-1 if((dividend<0)^(divisor<0))else 1)
     #make both dividend and divisor +ve
    dividend=abs(dividend)
    divisor=abs(divisor)
    quotient=0
    tempNumber=0
    for i in range(31,-1,-1):
        if(tempNumber+(divisor<<i)<=dividend):
            tempNumber+=divisor<<1
            quotient|=1<<i
    if sign==-1:
        quotient=-quotient
    return quotient
a=int(input("Enter the dividend:"))
b=int(input("Enter the divisor:"))
print("Results:",divide(a,b))