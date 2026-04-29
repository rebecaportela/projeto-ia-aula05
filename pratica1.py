"""
Módulo para verificação de números primos.

Este módulo contém uma função otimizada para determinar se um número é primo,
seguindo boas práticas de desenvolvimento Python.
"""


def eh_primo(numero: int) -> bool:
    """
    Verifica se um número é primo.
    
    Args:
        numero: Um inteiro a ser verificado.
    
    Returns:
        True se o número é primo, False caso contrário.
    
    Raises:
        ValueError: Se o número for menor que 1.
    
    Examples:
        >>> eh_primo(7)
        True
        >>> eh_primo(10)
        False
    """
    if numero < 1:
        raise ValueError("O número deve ser maior que 0.")
    
    if numero <= 1:
        return False
    
    # Números pares (exceto 2) não são primos
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    
    # Verifica apenas números ímpares até a raiz quadrada
    for i in range(3, int(numero ** 0.5) + 1, 2):
        if numero % i == 0:
            return False
    
    return True


def obter_numero_valido() -> int:
    """
    Obtém um número inteiro válido do usuário.
    
    Returns:
        Um inteiro válido fornecido pelo usuário.
    """
    while True:
        try:
            numero = int(input("Digite um número inteiro positivo: "))
            if numero < 1:
                print("Por favor, digite um número maior que 0.")
                continue
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")


def main() -> None:
    """Função principal do programa."""
    try:
        numero = obter_numero_valido()
        
        if eh_primo(numero):
            print(f"✓ {numero} é um número primo!")
        else:
            print(f"✗ {numero} NÃO é um número primo.")
    
    except KeyboardInterrupt:
        print("\n\nPrograma interrompido pelo usuário.")
    except Exception as e:
        print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    main()
