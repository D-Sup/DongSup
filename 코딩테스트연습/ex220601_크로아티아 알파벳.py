# baekjoon 2941
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
N = input()
for i in cro:
        N=N.replace(i,"*")   
print(len(N))