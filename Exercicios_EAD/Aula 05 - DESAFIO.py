i1 = 'True'
i2 = 'False'
A = str(input('Como está o interruptor A? (Digite "True" para ligado, e "False" para desligado) \n'))
B = str(input('Como está o interruptor B? (Digite "True" para ligado, e "False" para desligado) \n'))
C = str(input('Como está o interruptor C? (Digite "True" para ligado, e "False" para desligado) \n'))

acende = ((A and B == i1) and (C == i2))

print(acende)
