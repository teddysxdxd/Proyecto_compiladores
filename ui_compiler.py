"""
interfaz.py - Interfaz gráfica con Textual
"""

import os
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Static, RichLog
from textual.containers import Container, Horizontal
from textual.screen import Screen


class CompilacionScreen(Screen):
    
    CSS = """
    #volver-btn { dock: top; margin: 1; width: 20; }
    #compilacion-output { height: 1fr; margin: 1; border: solid $primary; }
    """
    
    def __init__(self, archivo, pipeline_func):
        super().__init__()
        self.archivo = archivo
        self.pipeline_func = pipeline_func
    
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Button("⬅️ Volver al menú", id="volver-btn", variant="primary")
        yield RichLog(id="compilacion-output", highlight=True, markup=False, auto_scroll=True)
        yield Footer()
    
    def on_mount(self) -> None:
        self.title = f"⚙️ Compilando: {os.path.basename(self.archivo)}"
        self.output = self.query_one("#compilacion-output", RichLog)

        self.output.write(f"⏳ Compilando {self.archivo}...\n")

        # 🔥 ESTE ES EL CAMBIO CLAVE
        def enviar_linea(texto):
            self.output.write(texto)

        # Ejecuta el pipeline (usa el callback)
        self.pipeline_func(self.archivo, enviar_linea)

        self.output.write("\n✅ PIPELINE COMPLETADO")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "volver-btn":
            self.app.pop_screen()


class MenuScreen(Screen):
    
    CSS = """
    Screen { align: center middle; }

    #menu-container {
        width: 55;
        height: auto;
        border: solid $primary;
        background: $surface;
        padding: 1 2;
    }

    #titulo {
        text-align: center;
        background: $primary;
        padding: 1;
        margin-bottom: 1;
    }

    #file-path {
        text-align: center;
        padding: 1;
        margin: 1 0;
        background: $panel;
        color: $success;
    }

    #estado {
        text-align: center;
        padding: 1;
        margin: 1 0;
        background: $panel;
    }

    #botones {
        margin: 1 0;
        align: center middle;
        width: 100%;
    }

    #botones Button {
        margin: 0 1;
        min-width: 15;
    }

    #exit-bar {
    text-align: center;
    margin-top: 1;
    padding: 1;
    background: red;
    color: rgb(255,255,255);
    text-style: bold reverse;
}
    """
    
    def __init__(self, seleccionar_archivo_func, pipeline_func):
        super().__init__()
        self.archivo_seleccionado = None
        self.seleccionar_archivo = seleccionar_archivo_func
        self.run_pipeline = pipeline_func
    
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)

        yield Container(
            Static("[bold]🧮 COMPILADOR PIPELINE[/bold]", id="titulo"),
            Static("📂 Ningún archivo seleccionado", id="file-path"),
            Static("✨ Selecciona un archivo y compila", id="estado"),

            Horizontal(
                Button("📂 Cargar", id="cargar", variant="primary"),
                Button("⚙️ Compilar", id="compilar", variant="success"),
                Button("🧹 Limpiar", id="limpiar", variant="warning"),
                id="botones",
            ),

            # 🔴 AQUÍ ESTÁ LA BARRA
            Static("⚠️  Presiona Ctrl + Q para salir", id="exit-bar"),

            id="menu-container",
        )

        yield Footer()

    def on_mount(self) -> None:
        self.title = "Compilador Pipeline"

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "cargar":
            self.cargar_archivo()
        elif event.button.id == "compilar":
            self.compilar()
        elif event.button.id == "limpiar":
            self.limpiar()

    def cargar_archivo(self):
        archivo = self.seleccionar_archivo()
        if archivo:
            self.archivo_seleccionado = archivo
            self.query_one("#file-path", Static).update(f"📂 {archivo}")
            self.query_one("#estado", Static).update("[green]✅ Archivo cargado[/]")
            self.notify("✅ Archivo cargado")
        else:
            self.notify("No se seleccionó archivo", severity="warning")

    def compilar(self):
        if not self.archivo_seleccionado:
            self.query_one("#estado", Static).update("[red]❌ Selecciona un archivo primero[/]")
            self.notify("❌ Selecciona un archivo primero", severity="error")
            return

        self.app.push_screen(
            CompilacionScreen(self.archivo_seleccionado, self.run_pipeline)
        )

        self.query_one("#estado", Static).update("[green]✅ Compilación finalizada[/]")

    def limpiar(self):
        self.archivo_seleccionado = None
        self.query_one("#file-path", Static).update("📂 Ningún archivo seleccionado")
        self.query_one("#estado", Static).update("✨ Selecciona un archivo y compila")
        self.notify("🧹 Limpiado")

class CompiladorApp(App):
    def __init__(self, seleccionar_archivo_func, pipeline_func):
        super().__init__()
        self.seleccionar_archivo = seleccionar_archivo_func
        self.run_pipeline = pipeline_func
    
    def on_mount(self) -> None:
        self.push_screen(MenuScreen(self.seleccionar_archivo, self.run_pipeline))