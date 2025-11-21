import json
import os

DATA_FILE = "player_data.json"

def cargar_datos():
    estructura_base = {
        "nombre": None,
        "xp": 0, 
        "nivel": 1, 
        "misiones_completadas": []
    }
    
    if not os.path.exists(DATA_FILE):
        return estructura_base
    
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        datos = json.load(f)
        # Asegurar que todos los campos existan (por si actualizamos versiones)
        for key, value in estructura_base.items():
            if key not in datos:
                datos[key] = value
        return datos

def guardar_datos(datos):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4)

def registrar_nombre(nuevo_nombre):
    datos = cargar_datos()
    datos["nombre"] = nuevo_nombre
    guardar_datos(datos)
    return datos

def recompensar(mision_id, xp_ganada):
    datos = cargar_datos()
    
    if mision_id in datos["misiones_completadas"]:
        # Si ya la hizo, no damos XP, pero no mostramos error
        return

    datos["xp"] += xp_ganada
    datos["misiones_completadas"].append(mision_id)
    
    # Sistema de niveles: Nivel = (XP // 100) + 1
    nuevo_nivel = (datos["xp"] // 100) + 1
    datos["nivel"] = nuevo_nivel

    guardar_datos(datos)