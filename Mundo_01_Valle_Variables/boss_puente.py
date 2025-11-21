def calcular_edad_magica(anio_nacimiento_texto):
    # 1. Convierte el texto a número entero (int)
    anio_numero = int(anio_nacimiento_texto)
    
    # 2. Calcula la edad (asumiendo año actual 2025)
    edad = 2025 - anio_numero
    
    # 3. Retorna la frase exacta
    return f"Tengo {edad} años"

if __name__ == "__main__":
    # Esta parte permite que tu cuñado JUEGUE en la terminal
    print("👹 GOLEM: ¡ALTO AHÍ! ¿EN QUÉ AÑO NACISTE, MORTAL?")
    respuesta_usuario = input("> ")
    
    resultado = calcular_edad_magica(respuesta_usuario)
    print(f"🧝 TÚ: {resultado}")