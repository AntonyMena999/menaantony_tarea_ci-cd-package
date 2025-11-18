
🚀 CI/CD con Python + GitHub Actions
📦 Construcción automática de Package + Pruebas + Artefactos

Autor: Antony Mena — 2025

✨ Objetivo del Proyecto

Este proyecto implementa un pipeline completo de CI/CD utilizando GitHub Actions, cumpliendo con:

✅ Ejecución de pruebas unitarias

✅ Construcción de un package Python

✅ Generación de artefactos .whl y .tar.gz

✅ Automatización completa del pipeline

✅ Documentación clara para la rúbrica

📁 Estructura del Proyecto
tarea_ci_cd/
├── app.py                 # Funciones principales del proyecto
├── pyproject.toml         # Configuración del package y del build
├── requirements.txt       # Dependencias del proyecto
├── README.md              # Documentación del proyecto
├── tests/
│   └── test_app.py        # Prueba unitaria
└── .github/
    └── workflows/
        └── ci.yml         # Pipeline CI/CD con GitHub Actions

📄 Descripción detallada de cada archivo

🟥 .github/workflows/ci.yml

Archivo que define todo el pipeline de CI/CD utilizando GitHub Actions.
Controla cada paso automático que ocurre cuando haces un push o pull request a main o master.

# .github/workflows/ci.yml
# --------------------------------------------------------
# Archivo principal del pipeline CI/CD.
# Ejecuta:
#   1. Instalación de Python
#   2. Instalación de dependencias
#   3. Ejecución de pruebas
#   4. Construcción del package
#   5. Publicación de artefactos
# --------------------------------------------------------

name: CI/CD Python                     # Nombre del workflow

on:
  push:                                # Se ejecuta al hacer push
    branches: [ "main", "master" ]
  pull_request:                        # Se ejecuta en Pull Requests
    branches: [ "main", "master" ]

jobs:
  build:
    runs-on: ubuntu-latest             # Sistema operativo para ejecutar el pipeline

    steps:
      - name: 📥 Checkout del repositorio
        uses: actions/checkout@v3      # Descarga el código del repositorio

      - name: 🐍 Configurar versión de Python
        uses: actions/setup-python@v4  
        with:
          python-version: '3.10'       # Versión de Python para el workflow

      - name: 📦 Instalar dependencias
        run: |
          python -m pip install --upgrade pip
          pip install pytest build     # Instala pruebas y herramientas de construcción

      - name: 🧪 Ejecutar pruebas
        run: pytest                    # Ejecuta todas las pruebas unitarias

      - name: 🧱 Construir package
        run: python -m build           # Genera .whl y .tar.gz en /dist

      - name: 📤 Subir artefacto generado
        uses: actions/upload-artifact@v3
        with:
          name: package                # Nombre del artefacto generado
          path: dist/                  # Carpeta donde se guardan los archivos construidos

¿Qué hace este archivo?

Define el pipeline completo de CI/CD.

Instala Python y las dependencias necesarias.

Ejecuta las pruebas del proyecto automáticamente.

Construye el paquete usando python -m build.

Genera y guarda los artefactos (.whl y .tar.gz).

Permite ver los artefactos en la sección “Actions” de GitHub.

Este archivo cumple con los puntos de la rúbrica:

✔ Configuración CI/CD funcional
✔ Pruebas automatizadas
✔ Construcción del package
✔ Artefactos generados correctamente


🟦 app.py

Archivo principal del proyecto. Contiene la función que se usará en el package y en las pruebas.

def suma(a, b):
    """Retorna la suma de dos números."""
    return a + b

if __name__ == "__main__":
    print("Resultado de suma(2,3):", suma(2, 3))


Este archivo permite:

Probar directamente el programa.

Tener funciones que serán empaquetadas.

Realizar pruebas unitarias.

🟩 pyproject.toml

Archivo que configura el paquete Python, define metadatos y permite construir los archivos .whl y .tar.gz mediante:

python -m build


Contenido explicado:

# pyproject.toml
# --------------------------------------------------------
# Archivo de configuración del package Python.
# Permite construir .whl y .tar.gz usando:
#   python -m build
# --------------------------------------------------------

[project]
name = "tarea-ci-cd"                   # Nombre del package
version = "0.1.0"                      # Versión del package
description = "Ejemplo detallado de CI/CD con Python"
authors = [{name="Antony Mena"}]       # Autor del proyecto
requires-python = ">=3.8"              # Versión mínima de Python

[build-system]
requires = ["setuptools", "wheel"]     # Herramientas de construcción
build-backend = "setuptools.build_meta" # Backend para crear artefactos

[tool.pytest.ini_options]
pythonpath = [
    "."                                 # Permite que pytest importe app.py
]


Este archivo es obligatorio para que python -m build funcione correctamente.

🟨 requirements.txt

Contiene las dependencias necesarias para pruebas y construcción:

pytest
build


Permite instalarlas con:

pip install -r requirements.txt

🟧 tests/test_app.py

Prueba unitaria del proyecto:

from app import suma

def test_suma():
    assert suma(2, 3) == 5


Valida que la función principal funciona correctamente.

🟥 .github/workflows/ci.yml

Archivo del pipeline de GitHub Actions.
Automatiza todo el ciclo CI/CD:

Descarga el repositorio

Instala Python

Instala dependencias

Ejecuta pruebas

Construye el package

Guarda los artefactos generados

Este archivo cumple estrictamente con el punto de la rúbrica sobre CI/CD.

⚙️ ¿Cómo funciona el CI/CD?
1️⃣ Realizas un push o un pull request

Cada vez que subes algo al repositorio:

2️⃣ GitHub Actions se ejecuta automáticamente

Incluye estos pasos:

pytest → ejecuta las pruebas

python -m build → construye el package

upload-artifact → sube los archivos de dist/

3️⃣ Resultado final del pipeline

En la sección Actions, se generarán estos artefactos:

dist/
  tarea_ci_cd-0.1.0-py3-none-any.whl
  tarea_ci_cd-0.1.0.tar.gz

🧪 Ejecutar pruebas localmente
pytest


Salida esperada:

1 passed

🧱 Construir el package localmente
python -m build


Esto generará la carpeta:

dist/

📦 Instalar tu propio package (prueba final)
pip install dist/*.whl


Luego prueba:

from app import suma
print(suma(10, 5))   # 15

👤 Autor

Antony Mena – 2025