def count_bits(n):
    #create a function to count the number of bits
    countzeros = 0
    countones = 0
    #number>than 0 then we all perfotm right shift 
    while(n):
        if(n&1==1):
            countones+=1
             #increase the cou8nt of ones
        else:
            countzeros+=1
            #increase the count of zeros
    #right shift to remove the last bit that we check
        n>>=1
    print("numberof ones:",countones,"\nNumber of zeros:",countzeros)
number=int(input("Enter the number:"))
count_bits(number)