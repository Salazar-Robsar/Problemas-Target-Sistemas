def Sequencia_Fibonacci(n):
    if n < 0:
        return '\nNumero invalido, escolher numero positivo\n'
    elif n == 0 or n == 1:
        return f'\nO numero {Numero} faz parte da sequencia fibonacci\n'
    else:
        fibo1 = 0
        fibo2 = 1
        fibo3 = 1   
        while fibo1 < Numero:
            fibo1 = fibo2 + fibo3
            fibo3 = fibo2
            fibo2 = fibo1
        if fibo1 == Numero:
            return f'\nO numero {Numero} faz parte da sequencia fibonacci\n'
        else:
            return f'\nO numero {Numero} não faz parte da sequencia fibonacci\n'

Numero = int(input())
Fibonacci = Sequencia_Fibonacci(Numero)
print(Fibonacci)
