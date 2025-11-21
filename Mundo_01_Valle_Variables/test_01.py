from script_01 import grito_sagrado
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import gamemaster

def probar():
    try:
        respuesta = grito_sagrado()
        assert respuesta == "¡Por Pyterra!", f"Gritaste '{respuesta}', pero se esperaba '¡Por Pyterra!'"
        gamemaster.recompensar("Mision_01", 50)
    except Exception as e:
        print(f"Algo salió mal: {e}")

if __name__ == "__main__":
    probar()