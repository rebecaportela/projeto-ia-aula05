```python
"""
Módulo para verificação de números primos.

Este módulo fornece funções para:
- Validar entrada do usuário
- Verificar se um número é primo de forma otimizada
- Executar o programa principal com tratamento de erros
"""

from math import isqrt


def eh_primo(numero: int) -> bool:
    """
    Determina se um número inteiro positivo é primo.

    Args:
        numero (int): Número a ser analisado.

    Returns:
        bool: True se o número for primo, False caso contrário.

    Raises:
        TypeError: Se o valor informado não for inteiro.
        ValueError: Se o número for menor que 1.

    Examples:
        >>> eh_primo(2)
        True
        >>> eh_primo(9)
        False
    """
    if not isinstance(numero, int):
        raise TypeError("O valor deve ser um número inteiro.")

    if numero < 1:
        raise ValueError("O número deve ser maior que 0.")

    # Casos base
    if numero == 1:
        return False
    if numero == 2:
        return True

    # Elimina números pares maiores que 2
    if numero % 2 == 0:
        return False

    # Testa divisores ímpares até a raiz quadrada
    limite = isqrt(numero)
    for divisor in range(3, limite + 1, 2):
        if numero % divisor == 0:
            return False

    return True


def obter_numero_valido() -> int:
    """
    Solicita ao usuário um número inteiro positivo válido.

    Returns:
        int: Número inteiro positivo fornecido pelo usuário.
    """
    while True:
        try:
            entrada = input("Digite um número inteiro positivo: ").strip()
            numero = int(entrada)

            if numero < 1:
                print("Por favor, informe um número maior que zero.")
                continue

            return numero

        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")


def exibir_resultado(numero: int) -> None:
    """
    Exibe na tela se o número é primo ou não.

    Args:
        numero (int): Número analisado.
    """
    mensagem = (
        f"✓ {numero} é um número primo!"
        if eh_primo(numero)
        else f"✗ {numero} NÃO é um número primo."
    )
    print(mensagem)


def main() -> None:
    """
    Função principal do programa.
    """
    try:
        numero = obter_numero_valido()
        exibir_resultado(numero)

    except KeyboardInterrupt:
        print("\n\nPrograma interrompido pelo usuário.")

    except (TypeError, ValueError) as erro:
        print(f"Erro: {erro}")

    except Exception as erro:
        print(f"Erro inesperado: {erro}")


if __name__ == "__main__":
    main()
```
