# 🚀 CI/CD con Python + GitHub Actions

### 📦 Construcción automática de Package + Pruebas + Artefactos

**Autor:** Antony Mena --- 2025

------------------------------------------------------------------------

## ✨ Objetivo del Proyecto

Este proyecto implementa un pipeline completo de **CI/CD utilizando
GitHub Actions**, cumpliendo con:

-   ✅ Ejecución de pruebas unitarias\
-   ✅ Construcción de un package Python\
-   ✅ Generación de artefactos `.whl` y `.tar.gz`\
-   ✅ Automatización completa del pipeline\
-   ✅ Documentación clara para la rúbrica

------------------------------------------------------------------------

## 📁 Estructura del Proyecto

    tarea_ci_cd/
    ├── app.py                  # Funciones principales
    ├── pyproject.toml          # Configuración del package
    ├── requirements.txt        # Dependencias
    ├── README.md               # Documentación
    ├── tests/
    │   └── test_app.py         # Prueba unitaria
    └── .github/
        └── workflows/
            └── ci.yml          # Pipeline CI/CD

------------------------------------------------------------------------

## 📄 Descripción detallada de cada archivo

------------------------------------------------------------------------

# 🟥 `.github/workflows/ci.yml`

Archivo que define todo el pipeline de CI/CD utilizando **GitHub
Actions**.\
Controla cada paso automático cuando haces *push* o *pull request* a
`main` o `master`.

### 📌 Contenido:

    name: CI/CD Python

    on:
      push:
        branches: [ "main", "master" ]
      pull_request:
        branches: [ "main", "master" ]

    jobs:
      build:
        runs-on: ubuntu-latest

        steps:
        - name: 📥 Checkout del repositorio
          uses: actions/checkout@v3

        - name: 🐍 Configurar versión de Python
          uses: actions/setup-python@v4
          with:
            python-version: '3.10'

        - name: 📦 Instalar dependencias
          run: |
            python -m pip install --upgrade pip
            pip install pytest build

        - name: 🧪 Ejecutar pruebas
          run: pytest

        - name: 🧱 Construir package
          run: python -m build

        - name: 📤 Subir artefacto generado
          uses: actions/upload-artifact@v3
          with:
            name: package
            path: dist/

### ✔ ¿Qué hace este archivo?

-   Define el pipeline completo de CI/CD\
-   Instala Python y dependencias\
-   Ejecuta pruebas automáticamente\
-   Construye el package\
-   Genera artefactos `.whl` y `.tar.gz`\
-   Permite descargarlos desde la pestaña **Actions** en GitHub

Cumple con los puntos de la rúbrica: - ✔ CI/CD funcional\
- ✔ Pruebas automatizadas\
- ✔ Construcción del package\
- ✔ Artefactos generados

------------------------------------------------------------------------

# 🟦 `app.py`

    def suma(a, b):
        \"\"\"Retorna la suma de dos números.\"\"\"
        return a + b

    if __name__ == "__main__":
        print("Resultado de suma(2,3):", suma(2, 3))

Este archivo permite: - Probar directamente el programa\
- Contener funciones para empaquetado\
- Ejecutar pruebas unitarias

------------------------------------------------------------------------

# 🟩 `pyproject.toml`

Archivo que configura el paquete Python y permite construirlo con:

    python -m build

Contenido:

    [project]
    name = "tarea-ci-cd"
    version = "0.1.0"
    description = "Ejemplo detallado de CI/CD con Python"
    authors = [{name="Antony Mena"}]
    requires-python = ">=3.8"

    [build-system]
    requires = ["setuptools", "wheel"]
    build-backend = "setuptools.build_meta"

    [tool.pytest.ini_options]
    pythonpath = [
        "."
    ]

Este archivo es obligatorio para generar `.whl` y `.tar.gz`.

------------------------------------------------------------------------

# 🟨 `requirements.txt`

Dependencias:

    pytest
    build

Instalación:

    pip install -r requirements.txt

------------------------------------------------------------------------

# 🟧 `tests/test_app.py`

    from app import suma

    def test_suma():
        assert suma(2, 3) == 5

Prueba unitaria que valida la función principal.

------------------------------------------------------------------------

# ⚙️ ¿Cómo funciona el CI/CD?

### 1️⃣ Haces un push o un pull request

GitHub Actions detecta automáticamente los cambios.

### 2️⃣ El pipeline ejecuta:

-   `pytest` → Ejecuta pruebas\
-   `python -m build` → Construye el package\
-   `upload-artifact` → Sube los artefactos

### 3️⃣ Artefactos generados en `dist/`

    tarea_ci_cd-0.1.0-py3-none-any.whl
    tarea_ci_cd-0.1.0.tar.gz

------------------------------------------------------------------------

# 🧪 Ejecutar pruebas localmente

    pytest

Salida esperada:

    1 passed

------------------------------------------------------------------------

# 🧱 Construir package localmente

    python -m build

Esto generará la carpeta `dist/`.

------------------------------------------------------------------------

# 📦 Instalar tu propio package

    pip install dist/*.whl

Probar:

    from app import suma
    print(suma(10, 5))

------------------------------------------------------------------------

# 👤 Autor

**Antony Mena -- 2025**
