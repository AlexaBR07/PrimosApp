def es_primo(n):
    """Determina si un número es primo."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

def filtrar_primos(array):
    """Filtra los números primos de un array de enteros."""
    if not isinstance(array, list):
        raise TypeError("Se esperaba una lista de enteros")
    return [x for x in array if isinstance(x, int) and es_primo(x)]