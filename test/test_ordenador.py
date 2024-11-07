# test/test_ordenador.py
import unittest
from main.ordenador import Ordenador


class TestOrdenador(unittest.TestCase):

    def test_merge_sort_lista_desordenada(self):
        # Prueba para una lista desordenada
        lista = [5, 3, 8, 1]
        ordenador = Ordenador(lista)
        resultado = ordenador.merge_sort()
        self.assertEqual(resultado, [1, 3, 5, 8])

    def test_merge_sort_lista_ordenada(self):
        # Prueba para una lista que ya está ordenada
        lista = [1, 2, 3, 4]
        ordenador = Ordenador(lista)
        resultado = ordenador.merge_sort()
        self.assertEqual(resultado, [1, 2, 3, 4])

    def test_merge_sort_lista_vacia(self):
        # Prueba para una lista vacía
        lista = []
        ordenador = Ordenador(lista)
        resultado = ordenador.merge_sort()
        self.assertEqual(resultado, [])

    def test_merge_sort_un_elemento(self):
        # Prueba para una lista con un solo elemento
        lista = [10]
        ordenador = Ordenador(lista)
        resultado = ordenador.merge_sort()
        self.assertEqual(resultado, [10])

    def test_generar_lista(self):
        # Prueba para el método generar_lista
        tamano = 5
        rango = 10
        lista = Ordenador.generar_lista(tamano, rango)
        self.assertEqual(len(lista), tamano)
        self.assertTrue(all(0 <= x <= rango for x in lista))


if __name__ == "__main__":
    unittest.main()
