q = 0
s = 0
n = float(input('Digite um número real: '))
while n != 0:
    q += 1
    s += n
    n = float(input('Digite um número real: '))
m = s / q
print('Foram digitados {} números e a média é {:.2f}'.format(q, m)) 