# 백준 2438번
x = int(input())
for i in range(1,10) :
    print(x, i, sep=' * ', end=' = ')
    print(x*i)
    #print(x, ' * ', i, ' = ', x*i)