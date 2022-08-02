# baekjoon 1676
h = 1
R = 0
for i in range(int(input()),1,-1):
    h*=i
M = str(h)
for j in M[::-1]:
    if j == '0':
        R+=1
    else:
        print(R)
        break
    
# new method
def f(x):
    return x*f(x-1) if x else 1
N = str(f(int(input())))[::-1]
print(N)
for NN in N:
    if int(NN):
        print(N.index(NN))
        break
