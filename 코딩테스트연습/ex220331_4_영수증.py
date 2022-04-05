# 백준 5565번
m,n=map(int,input().split())
count=0
for i in range(1,max(m,n)+1):
    if m%i==0 and n%i==0:
        count=i
print(count)
print(m//count*n)
