# Bit string 

# Name : Sritish Kumar Gouda
# Reg_No: 2341007051
# CSES prompt: https://cses.fi/problemset/task/1617

n=int(input())

# << -------- STRING METHOD -------- >> 

# You can try the string method where we generate the bin() of all number one by one and check their len(),
# if the length is greater than n than we break. 

# Wont work on CSES. As it will take a lot of time to just go through all the numbers. 
# Lets say you want to find all binary numbers of 50 bit. Which would be 1125899906842624, It simply wont work in the time frame.  
'''
l=1
i=0                        
while l<=n:
    print(i,bin(i)[2:])     
    i+=1
    if len(bin(i)[2:])>l:
        l=len(bin(i)[2:])
print(i)

'''

# << -------- EXPERIMENTAL METHOD -------- >>

# If you see any binary number can have only 2 digits 1 or 0
# Lets say you want to print all the binary numbers of length 5.
# That will include all binary numbers of length 1,2,3,4 and 5.
# and all binary numbers can have only 0 or 1. That makes it 2*2*2*2*2 possible numbers. 

print(2**n%(10**9+7))         # Since it is asked to print in %(10^9+7) format

