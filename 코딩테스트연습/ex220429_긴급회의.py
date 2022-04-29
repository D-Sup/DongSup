# 백준 20113번
import sys
r = []
n = int(sys.stdin.readline())
l = list(map(int,sys.stdin.readline().split()))
result = [0 for _ in range(n)]
for i in l:
    if i != 0:
        result[i-1]+=1
        m = max(result)
for j in range(n):
    if result[j] == m:
        r.append(j+1)
if len(r) >= 2:
    print("skipped")
else:
    print(r[0])
        

    