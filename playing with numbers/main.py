number = int(input("Enter a number:"))
#store the original numberin a variable for comparisions
original_number=number
reversed_number=0
#reverse the number
while number>0:#check if the number entered by useris greater than 0
    digit=number%10
    reversed_number=reversed_number*10+digit
    number//=10
#check if original_number is the same as reversed_number
if original_number==reversed_number:
    print(original_number, "is a palindrome number")
else:
    print(original_number,"is not a palindrome number")
