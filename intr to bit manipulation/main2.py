#Program to check if a number is even or odd using bitwise operator
def check_odd_even(num):
    if num & 1:
        print(f"{num}is an odd number.")
    else:
        print(f"{num}is an even number.")
num=int(input("Enter a number: "))
check_odd_even (num)

