from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from rich.table import Table
from rich.progress import Progress, BarColumn, TextColumn
from rich.align import Align
from rich.text import Text
import gamemaster
import time

console = Console()

def obtener_rango(nivel):
    """Da un título épico según el nivel"""
    titulos = {
        1: "Novato de la Villa",
        2: "Escudero de Código",
        3: "Guerrero de Bucles",
        5: "Hechicero de Funciones",
        10: "Arquitecto de Software",
        99: "Dios del Python"
    }
    # Busca el título más cercano hacia abajo
    titulos_ordenados = sorted(titulos.keys())
    titulo_actual = "Aventurero Desconocido"
    for n in titulos_ordenados:
        if nivel >= n:
            titulo_actual = titulos[n]
    return titulo_actual

def mostrar_perfil():
    console.clear()
    datos = gamemaster.cargar_datos()

    # 1. LOGIN: Si no tiene nombre, se lo pedimos con estilo
    if not datos["nombre"]:
        console.print(Panel.fit("¡Bienvenido, Viajero!", style="bold blue"))
        nombre = console.input("[bold yellow]¿Cuál es tu nombre de Héroe?: [/]")
        datos = gamemaster.registrar_nombre(nombre)
        console.print(f"[green]¡Registrado como {nombre}![/]\n")
        time.sleep(1)
        console.clear()

    # 2. CÁLCULOS DE XP
    nivel_actual = datos['nivel']
    xp_actual = datos['xp']
    xp_siguiente_nivel = nivel_actual * 100
    xp_progreso = xp_actual % 100 # Cuánto lleva del nivel actual
    
    # Si acaba de subir de nivel exacto (ej. 200xp), el modulo es 0, pero queremos mostrar barra llena o vacía?
    # Para simplificar: Nivel 1 (0-99), Nivel 2 (100-199).
    # Meta del nivel actual:
    meta_nivel = 100 

    # 3. CONSTRUCCIÓN DE LA INTERFAZ GRÁFICA (TUI)
    
    # Título del Rango
    rango = obtener_rango(nivel_actual)
    texto_rango = Text(f"Rank: {rango}", style="italic magenta")

    # Tabla de Estadísticas
    stats_table = Table(show_header=False, box=None, padding=(0, 2))
    stats_table.add_row("📜 Misiones Completadas:", str(len(datos['misiones_completadas'])))
    stats_table.add_row("⚔️ XP Total:", str(xp_actual))
    stats_table.add_row("🔋 Nivel:", f"[bold cyan]{nivel_actual}[/]")

    # Barra de Progreso Visual
    # Usamos caracteres unicode para dibujar la barra manualmente dentro del panel
    porcentaje = min(xp_progreso, 100)
    bloques = int(porcentaje / 5) # 20 bloques = 100%
    barra_visual = f"[{'█' * bloques}{'░' * (20 - bloques)}] {xp_progreso}/100 XP"
    
    # Panel Principal (La Tarjeta)
    contenido = Align.center(
        f"\n[bold white scale=2]{datos['nombre']}[/]\n"
        f"{texto_rango}\n\n"
    )
    
    console.print(Panel(
        contenido, 
        title="[bold yellow]🐍 PYTHON QUEST - ID CARD[/]", 
        subtitle="[dim]Orden de los Programadores[/]",
        style="blue",
        padding=(1, 4)
    ))

    # Panel de Stats y Progreso
    console.print(Panel(
        stats_table,
        title="Estadísticas",
        style="green"
    ))

    console.print(Panel(
        Align.center(f"[bold yellow]Progreso al Nivel {nivel_actual + 1}[/]\n{barra_visual}"),
        style="red"
    ))

    console.print("\n[dim]Tip: Completa misiones ejecutando 'python test_mision.py' en cada carpeta[/]")

if __name__ == "__main__":
    try:
        mostrar_perfil()
    except KeyboardInterrupt:
        print("Saliendo...")