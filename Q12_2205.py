# Gray Code
# -------------------------------------------------

# Name : Sritish Kumar Gouda
# Reg_No: 2341007051
# CSES Promt: https://cses.fi/problemset/task/2205

# !!! DISCLAIMER !!! : WRONG ANSWER
# This is not complete. I am working on this. 
# This just print all binary numbers upto required len. Now i just have to work some way to sort this into a gray code. 
# No screenshot is added as this doesnt work

n=int(input())
l=1         # current len
i=0                       







while l<=n:
    if len(bin(i)[2:])!=n:                              # printing vales of the required len. Like 00 + 01
        print(i, (n-len(bin(i)[2:]))*'0'+bin(i)[2:])     
    else:
        print(i, bin(i)[2:])

    i+=1
    if len(bin(i)[2:])>l:
        l=len(bin(i)[2:])
    
# print(i)   # count

    # ........................