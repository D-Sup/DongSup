# 백준 2445번
N = int(input())
for i in range(1,N):
    print('*'*i+' '*((N-i)*2)+'*'*i)
for j in range(N,0,-1):
    print('*'*j+' '*((N-j)*2)+'*'*j)

# n = int(input())
# for i in range(2*n-1):
#     if i<n:
#         print("*"*(i+1) + " "*(2*(n-i)-2) + "*"*(i+1))
#     else:
#         print("*"*(2*n-i-1) + " "*(2*i-2*n+2) + "*"*(2*n-i-1))
