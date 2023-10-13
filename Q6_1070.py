# Permutation
# -------------------------------------------------

# Name : Sritish Kumar Gouda
# Reg_No: 2341007051
# CSES Promt: https://cses.fi/problemset/task/1070

n=int(input())

if n in [0,2,3]:
    print('NO SOLUTION')
else:

    out=[]
    i=1         # 
    rev=0       # For alternate adding ele into out
    
    if n%2==0:
        #print('Even')

        echk=int(n/2)           # Mid values 
        echk=[echk,echk+1]      #
        #print(echk)

        while True:
            if i in echk and n in echk:     # for mid values
                out.insert(0,echk.pop())
                out.append(echk.pop())
                break

            if rev==0:
                out.append(i)       # from front
                rev=1
                i+=1
            elif rev==1:
                out.append(n)       # from back
                n-=1
                rev=0

    else:
        #print('Odd')
        ochk=int((n+1)/2)   # Mid value 
        #print(ochk)

        while True:

            if i==ochk and n==ochk:     # for mid value
                out.insert(0,ochk)
                break
                
            elif rev==0:            # from front
                out.append(i)
                i+=1
                rev=1
                    
            elif rev==1:            # from back
                out.append(n)
                n-=1
                rev=0

    for i in out:
        print(i, end=' ')

# U dont have to do this much labour. I was stupid to try this.
# If u could see u could have just seperated the odd and even ones and stick them together. 
# Like [1,2,3,4,5] ------> [2,4,1,3,5] or [1,2,3,4] ------> [2,4,1,3]
# It just didn't click me. I got to see it after i submitted this one ON CSES.
# I didn't want to change this. It works fine for me :)