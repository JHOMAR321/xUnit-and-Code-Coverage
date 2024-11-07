# main/ordenador.py
import random


class Ordenador:
    def __init__(self, lista=None):
        self.lista = lista if lista is not None else []

    def merge_sort(self):
        """
        Ordena la lista usando el algoritmo Merge Sort de forma ascendente.
        """
        if len(self.lista) <= 1:
            return self.lista

        # Dividir la lista en dos mitades
        mid = len(self.lista) // 2
        izquierda = Ordenador(self.lista[:mid]).merge_sort()
        derecha = Ordenador(self.lista[mid:]).merge_sort()

        # Combinar las mitades ordenadas
        return self._merge(izquierda, derecha)

    def _merge(self, izquierda, derecha):
        """
        Método auxiliar para combinar dos listas ordenadas.
        """
        resultado = []
        i = j = 0

        # Combinar mientras hay elementos en ambas listas
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[j])
                j += 1

        # Agregar los elementos restantes
        resultado.extend(izquierda[i:])
        resultado.extend(derecha[j:])

        return resultado

    import random

    @staticmethod
    def generar_lista(tamano, rango):
        """
        Genera una lista de enteros aleatorios.
        :param tamano: Número de elementos en la lista.
        :param rango: Rango máximo para los valores (-rango a rango).
        :return: Lista de enteros.
        """
        return [random.randint(-rango, rango) for _ in range(tamano)]

