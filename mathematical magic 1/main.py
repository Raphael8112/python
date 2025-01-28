#take input from user
number= int(input("Enter your number:"))
#calculate the number
digits= len(str(number))
result=0
#variable to store the number
temp=number
while temp >0:
    digit=temp%10
    result+=digit**digits
    temp//=10
#display the rest
if number==result:
    print("Amstrong number")
else:
    print("Not an amstrong number")