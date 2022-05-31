# programmers 12969
a, b = map(int, input().strip().split(' '))
print(*["*"*a for _ in range(b)],sep='\n')