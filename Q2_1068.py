# Weird Algorithm
# -------------------------------------------------

# Name : Sritish Kumar Gouda
# Reg_No: 2341007051
# CSES Promt: https://cses.fi/problemset/task/1068/



n=int(input())
print(n,end=' ')
while n!=1:
    
    if n%2==0:
        #print('even')
        n=int(n/2)
        
    else:
        #print('odd')
        n=(n*3)+1
    
    print(n,end=' ')

    
