F = int(input('Введите первое число: '))
S = int(input('Введите второе число: '))
T = int(input('Введите третье число: '))
if F == S == T :
    print(3)
elif F == T or S == T or F == S :
    print(2)
elif not(F == S == T) :
    print(0)
