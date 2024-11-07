from main.ordenador import Ordenador

_sort = Ordenador()

# Lista de enteros
tamano = 5
rango = 10

list_number = _sort.generar_lista(tamano, rango)

# Imprimir la lista
print("Lista desordenada")
print(list_number)

# Ordenar lista
srt = Ordenador(list_number)
list_result = srt.merge_sort()

# Lista ordenada
print("Lista ordenada")
print(list_result)
