a= int(input('Введите число в десятичной системе счисления: '))
cc= int(input('Введите систему счисления, в которую вы хотите перевести число: '))
if cc == 2:
    b=bin(a)[2:]
if cc == 8:
    b=oct(a)[2:]
print(b)
