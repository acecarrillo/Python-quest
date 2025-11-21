from boss_puente import calcular_edad_magica
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import gamemaster

def batalla_final():
    print("⚔️ INICIANDO BATALLA CONTRA EL GOLEM...")
    try:
        # Ataque 1: Probar con un año normal
        # Le pasamos el número como "String" porque así viene del input() real
        assert calcular_edad_magica("2000") == "Tengo 25 años", "❌ El Golem te aplastó. Cálculo incorrecto para el año 2000."
        
        # Ataque 2: Probar con otro año
        assert calcular_edad_magica("1990") == "Tengo 35 años", "❌ El Golem bloqueó tu paso. Fallaste con el año 1990."

        print("✨ ¡GOLPE CRÍTICO! El Golem se aparta.")
        # Gran recompensa por matar al Boss
        gamemaster.recompensar("BOSS_Mundo_01", 200) 
        
    except ValueError:
        print("💀 MUERTE: Olvidaste convertir el texto a int() antes de restar.")
    except AssertionError as e:
        print(e)
    except Exception as e:
        print(f"💥 Error desconocido: {e}")

if __name__ == "__main__":
    batalla_final()