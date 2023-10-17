# Plaindome re-order
# -------------------------------------------------

# Name : Sritish Kumar Gouda
# Reg_No: 2341007051
# CSES Promt: https://cses.fi/problemset/task/1755/


# Note: If u find any letter occuring odd number of times is greater than 1. No solution
# String with 1 odd letter will work. The odd one will take the middle spot and all other even letters can be spread both 
# side of the string. 


import collections

s=input().strip()
l=dict(collections.Counter(s))          # If any letter are in odd number > 1. You can't arrange them  in plaindome
c=0
for i in l.values():
    if i%2==0:          # Counting the number of odd numbered letters
        continue
    else:
        c+=1
#print(l)
if c>1:
    print('NO SOLUTION')

else:
    rx=[]
    tx=[]
    od=[]
    for i in l:
        #print(i)
        if l[i]%2==0:
            # even
            rx.append(i*int(l[i]/2))
            tx.append(i*int(l[i]/2))
        else:
            # odd
            rx.append(i*int(l[i]/2))
            tx.append(i*int(l[i]/2))
            od.append(i*1)
            
    print(''.join(rx+od),end='')
    print(''.join(tx[::-1]))

# Dont use this method. It works fine but is silly. U dont have to do this much labour. U can just seperate the number into odd and even
# and stick them together.
# It just didnt click me and i didnt want to chage this. It works fine for me :)
