
# Explicação linha por linha do código Python (num.py)

## Código:
```python
def is_prime(n: int) -> bool:
    """
    Verifica se um número é primo.

    Args:
        n (int): O número a ser verificado.

    Returns:
        bool: True se o número for primo, False caso contrário.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Testes
print(is_prime(2))  # True
print(is_prime(3))  # True
print(is_prime(4))  # False
print(is_prime(17)) # True
print(is_prime(18)) # False
```

## Explicação linha por linha:

1. `def is_prime(n: int) -> bool:`  
   Define uma função chamada `is_prime` que recebe um parâmetro `n` do tipo inteiro e retorna um booleano. Esta função verifica se o número `n` é primo.

2. `"""`  
   Início da docstring (documentação da função).

3. `Verifica se um número é primo.`  
   Descrição da função na docstring.

4. `Args:`  
   Seção da docstring para argumentos.

5. `n (int): O número a ser verificado.`  
   Descrição do parâmetro `n`.

6. `Returns:`  
   Seção da docstring para o valor de retorno.

7. `bool: True se o número for primo, False caso contrário.`  
   Descrição do valor retornado.

8. `"""`  
   Fim da docstring.

9. `if n <= 1:`  
   Verifica se `n` é menor ou igual a 1. Números menores ou iguais a 1 não são considerados primos.

10. `return False`  
    Se a condição acima for verdadeira, a função retorna `False`, indicando que `n` não é primo.

11. `for i in range(2, int(n**0.5) + 1):`  
    Inicia um loop que itera sobre valores de `i` começando de 2 até a raiz quadrada de `n` (arredondada para baixo e somada 1). Isso é eficiente porque se `n` tem um divisor maior que sua raiz quadrada, o outro divisor será menor.

12. `if n % i == 0:`  
    Dentro do loop, verifica se `n` é divisível por `i` (ou seja, se o resto da divisão de `n` por `i` é zero).

13. `return False`  
    Se `n` for divisível por `i`, a função retorna `False`, pois `n` não é primo.

14. `return True`  
    Se o loop terminar sem encontrar nenhum divisor, a função retorna `True`, indicando que `n` é primo.

15. `# Testes`  
    Comentário indicando que as linhas seguintes são testes da função.

16. `print(is_prime(2))  # True`  
    Chama a função com 2 e imprime o resultado. 2 é primo, então imprime `True`.

17. `print(is_prime(3))  # True`  
    Chama a função com 3 e imprime o resultado. 3 é primo, então imprime `True`.

18. `print(is_prime(4))  # False`  
    Chama a função com 4 e imprime o resultado. 4 não é primo, então imprime `False`.

19. `print(is_prime(17)) # True`  
    Chama a função com 17 e imprime o resultado. 17 é primo, então imprime `True`.

20. `print(is_prime(18)) # False`  
    Chama a função com 18 e imprime o resultado. 18 não é primo, então imprime `False`.
