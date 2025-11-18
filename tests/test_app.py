
# tests/test_app.py
# --------------------------------------------------------
# Archivo de pruebas unitarias usando pytest.
# Verifica que la función 'suma' funciona correctamente.
# --------------------------------------------------------

from app import suma

def test_suma():
    assert suma(2, 3) == 5
