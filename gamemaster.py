import json
import os
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align

# --- CONFIGURACIÓN DE RUTAS (FIX #2) ---
# Obtenemos la ruta absoluta de DONDE está este archivo (gamemaster.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Forzamos a que el JSON siempre viva en esa ruta base
DATA_FILE = os.path.join(BASE_DIR, "player_data.json")

console = Console()

def cargar_datos():
    estructura_base = {
        "nombre": None,
        "xp": 0, 
        "nivel": 1, 
        "misiones_completadas": []
    }
    
    if not os.path.exists(DATA_FILE):
        return estructura_base
    
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            datos = json.load(f)
            # Mezclar con base por si agregamos campos nuevos a futuro
            for key, value in estructura_base.items():
                if key not in datos:
                    datos[key] = value
            return datos
    except Exception:
        return estructura_base

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
    
    # Si ya completó la misión, avisamos bonito pero no damos XP
    if mision_id in datos["misiones_completadas"]:
        console.print(Panel(
            f"[yellow]Ya completaste la misión '{mision_id}'.\nNo se otorga XP extra, pero tu código sigue funcionando perfecto.[/]",
            title="🔁 Misión Repetida",
            style="yellow",
            border_style="yellow"
        ))
        return

    # Lógica de XP y Nivel
    datos["xp"] += xp_ganada
    datos["misiones_completadas"].append(mision_id)
    
    nivel_anterior = datos["nivel"]
    nuevo_nivel = (datos["xp"] // 100) + 1
    datos["nivel"] = nuevo_nivel
    
    guardar_datos(datos)

    # --- SALIDA VISUAL (FIX #1) ---
    mensaje = Align.center(
        f"\n[bold white]¡Misión '{mision_id}' Completada![/]\n"
        f"[bold green]+{xp_ganada} XP[/]\n\n"
        f"[italic cyan]XP Total: {datos['xp']} | Nivel: {datos['nivel']}[/]"
    )
    
    console.print(Panel(
        mensaje,
        title="🎉 ¡VICTORIA! 🎉",
        style="bold green",
        border_style="green",
        padding=(1, 2)
    ))

    if nuevo_nivel > nivel_anterior:
        console.print(Panel(
            Align.center(f"🔥 ¡HAS SUBIDO AL NIVEL {nuevo_nivel}! 🔥"),
            style="bold magenta"
        ))