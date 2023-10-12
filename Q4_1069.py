# Repetition
# -------------------------------------------------

# Name : Sritish Kumar Gouda
# Reg_No: 2341007051
# CSES Promt: https://cses.fi/problemset/task/1069

s= input().strip() # 'ATTCGGGA'
c=''  # Cursor
l=''  # last rept.
max=0   # Temporary max
count=0 

for i in s:
    
    if c==i:
        count+=1

        if max<=count:
            
            l=i
            max=count
    elif c!=i:
        count=0        
    c=i
# print(l*(max+1), max+1)
print(max+1)