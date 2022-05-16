# baekjoon 1357
import sys
input = sys.stdin.readline
X, Y = list(map(str,input().split()))
Rev_X = "".join(reversed(X))
Rev_Y = "".join(reversed(Y))
Rev_X_Y = int(Rev_X) + int(Rev_Y)
Rev_X_Y = str(Rev_X_Y)
result = "".join(reversed(Rev_X_Y))
result = result.strip("0")
print(result)
