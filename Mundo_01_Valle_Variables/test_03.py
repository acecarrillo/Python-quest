from script_03 import calcular_factura
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import gamemaster

def probar():
    try:
        # Caso 1: Compra básica
        assert calcular_factura(10, 2, 1) == 21, "Error: 10 monedas * 2 pociones + 1 impuesto debería ser 21."
        
        # Caso 2: Compra grande
        assert calcular_factura(5, 10, 0) == 50, "Error: 5 * 10 + 0 debería ser 50."
        
        gamemaster.recompensar("Mision_03", 75)
    except Exception as e:
        print(f"Error en tus cálculos: {e}")

if __name__ == "__main__":
    probar()