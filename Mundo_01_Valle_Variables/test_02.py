from script_02 import equipar_personaje
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import gamemaster

def probar():
    try:
        datos = equipar_personaje()
        # Verificamos que existen
        assert datos is not None, "La mochila está vacía (retornaste None)"
        
        arma, pociones, hambre = datos
        
        # Verificamos Tipos y Valores
        assert arma == "Espada de Madera", "El arma incorrecta."
        assert isinstance(pociones, int), "Las pociones deben ser un número entero."
        assert pociones == 5, "Debes llevar exactamente 5 pociones."
        assert hambre is True, "Debes admitir que tienes hambre (True)."
        
        gamemaster.recompensar("Mision_02", 100)
    except NameError:
        print("Error: Una de tus variables no tiene el nombre correcto.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    probar()