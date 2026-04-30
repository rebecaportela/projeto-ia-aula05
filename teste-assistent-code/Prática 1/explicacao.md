# Explicação linha por linha do código Python (num.py)

## Código:
```python
def is_prime(n):
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

1. `def is_prime(n):`  
   Define uma função chamada `is_prime` que recebe um parâmetro `n`. Esta função verifica se o número `n` é primo.

2. `if n <= 1:`  
   Verifica se `n` é menor ou igual a 1. Números menores ou iguais a 1 não são considerados primos.

3. `return False`  
   Se a condição acima for verdadeira, a função retorna `False`, indicando que `n` não é primo.

4. `for i in range(2, int(n**0.5) + 1):`  
   Inicia um loop que itera sobre valores de `i` começando de 2 até a raiz quadrada de `n` (arredondada para baixo e somada 1). Isso é eficiente porque se `n` tem um divisor maior que sua raiz quadrada, o outro divisor será menor.

5. `if n % i == 0:`  
   Dentro do loop, verifica se `n` é divisível por `i` (ou seja, se o resto da divisão de `n` por `i` é zero).

6. `return False`  
   Se `n` for divisível por `i`, a função retorna `False`, pois `n` não é primo.

7. `return True`  
   Se o loop terminar sem encontrar nenhum divisor, a função retorna `True`, indicando que `n` é primo.

8. `# Testes`  
   Comentário indicando que as linhas seguintes são testes da função.

9. `print(is_prime(2))  # True`  
   Chama a função com 2 e imprime o resultado. 2 é primo, então imprime `True`.

10. `print(is_prime(3))  # True`  
    Chama a função com 3 e imprime o resultado. 3 é primo, então imprime `True`.

11. `print(is_prime(4))  # False`  
    Chama a função com 4 e imprime o resultado. 4 não é primo, então imprime `False`.

12. `print(is_prime(17)) # True`  
    Chama a função com 17 e imprime o resultado. 17 é primo, então imprime `True`.

13. `print(is_prime(18)) # False`  
    Chama a função com 18 e imprime o resultado. 18 não é primo, então imprime `False`.
