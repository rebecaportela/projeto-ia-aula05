def eh_primo(numero):
    if numero <= 1:
        return False
    
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    
    return True


numero = int(input("Digite um número: "))

if eh_primo(numero):
    print("É primo")
else:
    print("Não é primo")
