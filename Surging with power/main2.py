def is_power_of_four(n):
    if n<= 0:
        return False
    # Check if it is a power of 2 first
    if(n & (n-1)) !=0:
        return False
    # Check if the only set bit is at an even position (0-based)
    return (n-1) % 3 ==0
num = int(input("Enter a number:"))
if is_power_of_four(num):
    print(f"{num} is a power of 4.")
else:
    print(f"{num}is not a power of 4")
