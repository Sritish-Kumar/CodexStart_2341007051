# Number Spiral
# -------------------------------------------------

# Name : Sritish Kumar Gouda
# Reg_No: 2341007051
# CSES Promt: https://cses.fi/problemset/task/1071


# !!! DISCLAIMER !!! : TIME LIMIT EXCEEDED
# I tried to predict the number from an Formula or progression. Couldn't make one. 
# Therfore I had to make the entire number spiral of n rows and then get the required rows and column from it. 
# Works fine just is not efficient for bigger numbers. 


n= 200 # will make 100 rows spiral table

rx=[]
c=1
rev=3
for i in range(1,n,2):      # Number of element in a row 1,3,5,7,9,....
    
    l=[] 
    for j in range(i):                                          # ------------ making the diagonal stretched element
        #print(c)
        l.append(c)
        c+=1
    if (i-rev)==0:          # reversing the diagonal on alterante
        l.sort(reverse=True)
        rev+=4
    rx.append(l)    
    #print()
#print(rx)   #-------> Diagonal ele done

tx=[]                                                            # ----------- makking the matrix

def ele():
    global rx      # Popping ele from other diags
    
    x=[]
    for i in rx:
        
        try:
            x.append(i.pop())
        except:
            continue
    return x

#* print(rx)

for i in range(len(rx)):
    zx=[]
    t=0
    while True:            # Getting the entire ele from top row (diag.)
        try:
            zx.append(rx[i].pop(t))
        except:
            break
    #zx=zx[::-1]

    x=ele()
    zx+=x
    #* print('*',zx)
    tx.append(zx)  # appending each row

#print(tx)    # -------- matrix made contains each row in a list [[r1],[r2],[r3]...]


n=int(input())

for i in range(n):
    r1,*c1=list(map(int,input().strip().split(' ')))
    c1=c1[0]
    try:
        print(tx[r1-1][c1-1])
    except:
        print('INDEX OUT OF RANGE OF THE OBTAINED MATRIX')
        continue


