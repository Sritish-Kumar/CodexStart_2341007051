# Increasing array
# -------------------------------------------------

# Name : Sritish Kumar Gouda
# Reg_No: 2341007051
# CSES Promt: https://cses.fi/problemset/task/1094/

n=int(input())
x=list(map(int,input().strip().split(' ')))  # [6,10,4,10,2,8,9,2,7,7]  

c=0
t=0
max=0

for i in range(len(x)):
    if max<=x[i]:
        c=x[i]
        if c>max:
            max=c
        continue
    else:              # elif max>x[i]                          

        #print('*',max-x[i])
        t=t+(max-x[i])
        #print(t)
        c=x[i]
        continue
    
print(t)