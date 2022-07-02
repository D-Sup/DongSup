# baekjoon 2525
n,m = map(int,input().split())
p = int(input())
n+=p//60
m+=p%60
if m >= 60:
    n+=1
    m-=60
if n >= 24:
    n -= 24
print(n,m,sep=" ")