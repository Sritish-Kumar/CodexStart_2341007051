# Creating Strings
# -------------------------------------------------

# Name : Sritish Kumar Gouda
# Reg_No: 2341007051
# CSES Promt: https://cses.fi/problemset/task/1622/


import itertools

s=sorted(input())
rx=sorted(set(itertools.permutations(s)))


# tx=[]                     # manually seperating unique elements
# for i in list(rx):
#     if i not in tx:
#         tx.append(i)
# print(len(tx))
# for i in tx:
#     print(''.join(i))
# print(rx)


print(len(rx))
for i in rx:
    print(''.join(i))