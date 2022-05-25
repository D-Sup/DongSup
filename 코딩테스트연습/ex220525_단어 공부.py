# baekjoon 1157
import sys 
int = sys.stdin.readline
N = list(input())
M, K= [], []
for q in N:
    if ord(q) < 91:
        K.append(chr(ord(q) + 32))
    else:
        K.append(q)
A = 'abcdefghijklmnopqrstuvwxyz'
p = [0*len(A) for _ in A]
for j in K:
    if j in A:
        p[A.index(j)]+=1
for i in K:
    if  i == max(K, key=K.count):
        M.append(i)
if p.count(max(p)) > 1:
    print('?')
elif len(set(M)) == 1:
    print(chr(ord(M[0]) - 32))
    
# word = input().upper()
# word_list = list(set(word))
# cnt = []
# for i in word_list:
#   count = word.count
#   cnt.append(count(i))
# if cnt.count(max(cnt)) > 1:
#   print("?")
# else:
#   print(word_list[(cnt.index(max(cnt)))])