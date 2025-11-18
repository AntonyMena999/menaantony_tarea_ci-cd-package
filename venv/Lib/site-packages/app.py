
# app.py
# --------------------------------------------------------
# Este archivo contiene la lógica principal del proyecto.
# Incluye una función simple 'suma' usada para pruebas
# y para demostrar el CI/CD y construcción del package.
# --------------------------------------------------------

def suma(a, b):
    """Retorna la suma de dos números."""
    return a + b

if __name__ == "__main__":
    # Ejecución directa del script
    print("Resultado de suma(2,3):", suma(2,3))
