# Missing Number
# -------------------------------------------------

# Name : Sritish Kumar Gouda
# Reg_No: 2341007051
# CSES Promt: https://cses.fi/problemset/task/1083/

n=int(input().strip())
l=list(map(int, input().strip().split(' ')))

n=[i for i in range(1,n+1)]

print(sum(n)-sum(l))