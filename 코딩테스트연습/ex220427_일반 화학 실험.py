# น้มุ 4766น๘
s = float(input())
while True:
    a = input()
    if a == '999':
        break
    print('%.2f' %(float(a)-s))
    s = float(a)