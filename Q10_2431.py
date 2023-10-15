# Digit Queries
# -------------------------------------------------

# Name : Sritish Kumar Gouda
# Reg_No: 2341007051
# CSES Promt: https://cses.fi/problemset/task/2431/


# !!! DISCLAIMER !!! : Partial Submission
# Works fine for 2 test cases but Time Limit Exceed for other 2 test cases. 
# I tried another mathmatical method (trying to make the repetiting pattern)  without using string. I just couldnt do it.

s=" "
num=[]
r=int(input().strip())
for i in range(r):
    x=num.append(int(input()))

for i in range(1,max(num)):
    s+=f"{i}"

for i in (num):
    print(s[i-1])