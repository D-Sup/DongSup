# 백준 1864번
dict_ = {'-': 0, '\\': 1, '(': 2, '@': 3, '?': 4, '>': 5, '&': 6, '%': 7, '/': -1}
while True:
    str_ = input()
    if str_ == '#':
        break
    res = 0
    for i in range(len(str_)):
        res += dict_[str_[i]] * (8 ** (len(str_) - i -1))
    print(res)
