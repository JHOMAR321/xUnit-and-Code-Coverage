# xUnit-and-Code-Coverage

Este proyecto implementa el algoritmo de ordenamiento Merge Sort en Python y proporciona pruebas unitarias para verificar su correcta funcionalidad.

## Estructura del Proyecto

El proyecto está organizado en dos carpetas principales:

- **main:** Contiene el código fuente principal, incluyendo la clase `Ordenador` en el archivo `ordenador.py`.
- **test:** Contiene las pruebas unitarias para la clase `Ordenador` en el archivo `test_ordenador.py`.

## Instalación
Este proyecto utiliza la biblioteca estándar de Python, pero de ser necesario instalar las dependencias con:

```bash
pip install -r requirements.txt
```

## Ejecución

### Ejecutar las pruebas

Para ejecutar las pruebas unitarias, utiliza el siguiente comando:

```bash
python -m unittest discover -s test
```
### Generar informe de cobertura de código
Para generar un informe de cobertura de código, utiliza los siguientes comandos:
```bash
coverage run -m unittest discover -s test
coverage report
```

### Para generar un informe HTML más detallado, usa:
```bash
coverage html
```