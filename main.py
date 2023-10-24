def numeroPrimo():
    numeroPrimoStr = input('Digite um número: ')
    if numeroPrimoStr.isdigit() != True:
        print('Isto não é um número!')
        return
    else:
        numeroPrimo = int(numeroPrimoStr)
        if numeroPrimo > 1:
            for i in range(2, numeroPrimo):
                if (numeroPrimo % i) == 0:
                    print('Este número não é primo!')
                    break
                else:
                    print('Este número é primo!')
numeroPrimo()