# Trailing Zeros
# -------------------------------------------------

# Name : Sritish Kumar Gouda
# Reg_No: 2341007051
# CSES Promt: https://cses.fi/problemset/task/1618


n=int(input().strip())

# f=1                          # Calulating factorial 
# for i in range(2,n+1):
#     f*=i


# s=f'{f}'[::-1]
# c=0                  ----- >  # string method
# for i in s:
#     if i=='0':
#         c+=1
#         continue
#     else:
#         break
# print(c)


# c=0                  ----- >   # calculation method
# h=10
# while True:
#     if f%h==0:
#         c+=1
#         h*=10
#         #f=int(f/h)
#         continue
#     else:
#         break
# print(c)


# ------------- >  Factor method without calculating factorial

i=5
c=0
while True:
    if n//i==0:
        break
    #print(n,i,c)
    c+=n//i
    i*=5
    
    
print(c)


