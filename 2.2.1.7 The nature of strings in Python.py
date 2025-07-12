# Slices

alpha = "abdefg"

print(alpha[1:3])#bd 
print(alpha[3:])#efg
print(alpha[:3])#abd
print(alpha[3:-2])#e
print(alpha[-3:4])#e
print(alpha[::2])#adf
print(alpha[1::2])#beg

'''
**Rebanado de Cadenas en Python**
=====================================

El código de Python proporcionado demuestra varias formas de rebanar una cadena utilizando indexación.
A continuación, se explica cada línea:

### 1. `print(alpha[1:3])  # bd`

* `alpha[1:3]` extrae una subcadena de `alpha` comenzando en el índice 1 (inclusive) y terminando en el
índice 3 (exclusive).
* La subcadena resultante es `"bd"`.

### 2. `print(alpha[3:])  # efg`

* `alpha[3:]` extrae una subcadena de `alpha` comenzando en el índice 3 (inclusive) y continuando hasta
el final de la cadena.
* La subcadena resultante es `"efg"`.

### 3. `print(alpha[:3])  # abd`

* `alpha[:3]` extrae una subcadena de `alpha` comenzando en el principio de la cadena (índice 0) y
terminando en el índice 3 (exclusive).
* La subcadena resultante es `"abd"`.

### 4. `print(alpha[3:-2])  # e`

* `alpha[3:-2]` extrae una subcadena de `alpha` comenzando en el índice 3 (inclusive) y terminando en el
índice -2 (exclusive), que es equivalente al segundo carácter desde el final.
* La subcadena resultante es `"e"`.

### 5. `print(alpha[-3:4])  # e`

* `alpha[-3:4]` extrae una subcadena de `alpha` comenzando en el índice -3 (inclusive), que es equivalente
al tercer carácter desde el final, y terminando en el índice 4 (exclusive).
* La subcadena resultante es `"e"`.

### 6. `print(alpha[::2])  # adf`

* `alpha[::2]` extrae una subcadena de `alpha` comenzando en el principio de la cadena (índice 0) y avanzando
de 2 caracteres en 2.
* La subcadena resultante es `"adf"`.

### 7. `print(alpha[1::2])  # beg`

* `alpha[1::2]` extrae una subcadena de `alpha` comenzando en el índice 1 (inclusive) y avanzando de 2
caracteres en 2.
* La subcadena resultante es `"beg"`.

**Sintaxis General**
-------------------

La sintaxis general para rebanar cadenas en Python es:
```python
cadena[inicio:fin:paso]
```
Donde:

* `inicio`: El índice de inicio (inclusive).
* `fin`: El índice de fin (exclusive).
* `paso`: El tamaño del paso (por defecto es 1).

Al omitir alguno de estos valores, se pueden lograr diferentes comportamientos de rebanado. Por ejemplo:

* `cadena[inicio:]` comienza en `inicio` y continúa hasta el final de la cadena.
* `cadena[:fin]` comienza en el principio de la cadena y termina en `fin`.
* `cadena[::paso]` comienza en el principio de la cadena y avanza de `paso` caracteres en `paso`.

'''