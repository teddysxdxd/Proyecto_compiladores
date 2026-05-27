import os
from pathlib import Path

from rich.text import Text
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.screen import Screen
from textual.widgets import Button, Checkbox, Footer, Header, RichLog, Static

from ir_manual import (
    construir_diff_paralelo,
    ejecutar_ir_manual_targets,
    optimizar_ir_manual_archivo,
)


def limpiar_artefactos_generados_src(src_dir: str = "src"):
    src_path = Path(src_dir)
    if not src_path.exists():
        return {"ok": False, "error": f"No existe carpeta: {src_path}", "deleted": [], "errors": []}

    patrones = [
        "*.ll",
        "*.opt.ll",
        "*.tac",
        "*.linux.o",
        "*.windows.obj",
        "*.exe",
        "*_linux.bin",
        "*.manual.ll",
        "*.manual.export.ll",
        "*.manual.export.*.ll",
        "*.manual.run*",
    ]

    candidatos = set()
    for patron in patrones:
        for path in src_path.glob(patron):
            if path.is_file():
                candidatos.add(path)

    deleted = []
    errors = []

    for path in sorted(candidatos):
        try:
            path.unlink()
            deleted.append(str(path))
        except Exception as e:
            errors.append(f"{path}: {e}")

    return {"ok": len(errors) == 0, "deleted": deleted, "errors": errors}


class CompilacionScreen(Screen):
    CSS = """
    #volver-btn { dock: top; margin: 1; width: 22; }
    #compilacion-output { height: 1fr; margin: 1; border: solid $primary; }
    """

    def __init__(self, archivo, pipeline_func, targets_fase8=("linux", "windows")):
        super().__init__()
        self.archivo = archivo
        self.pipeline_func = pipeline_func
        self.targets_fase8 = tuple(targets_fase8)

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Button("Volver al menu", id="volver-btn", variant="primary")
        yield RichLog(id="compilacion-output", highlight=True, markup=False, auto_scroll=True)
        yield Footer()

    def on_mount(self) -> None:
        self.title = f"Compilando: {os.path.basename(self.archivo)}"
        self.output = self.query_one("#compilacion-output", RichLog)
        self.output.write(f"Compilando {self.archivo}...\n")
        self.output.write(f"Targets Fase 8: {', '.join(self.targets_fase8)}\n")

        def enviar_linea(texto):
            self.output.write(texto)

        self.pipeline_func(
            self.archivo,
            enviar_linea,
            targets_fase8=self.targets_fase8,
        )
        self.output.write("\nPIPELINE COMPLETADO")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "volver-btn":
            self.app.pop_screen()


class IRManualScreen(Screen):
    CSS = """
    #volver-manual-btn { dock: top; margin: 1; width: 22; }
    #manual-container {
        margin: 1;
        border: solid $accent;
        padding: 1 2;
        height: 1fr;
    }
    #manual-file {
        padding: 1;
        background: $panel;
        margin-bottom: 1;
    }
    #manual-passes-row1, #manual-passes-row2 {
        margin: 0 0 1 0;
        height: auto;
    }
    #manual-passes-row1 Checkbox, #manual-passes-row2 Checkbox {
        margin-right: 2;
        width: 1fr;
    }
    #manual-actions {
        margin: 0 0 1 0;
        height: auto;
    }
    #manual-targets {
        margin: 0 0 1 0;
        height: auto;
    }
    #manual-targets Checkbox {
        margin-right: 2;
        width: auto;
    }
    #manual-actions Button {
        margin-right: 1;
        min-width: 18;
    }
    #manual-output {
        height: 1fr;
        border: solid $primary;
    }
    """

    def __init__(self, archivo):
        super().__init__()
        self.archivo = archivo
        self.ir_base = os.path.splitext(archivo)[0] + ".ll"
        self.ir_manual = os.path.splitext(archivo)[0] + ".manual.ll"
        self.ir_actual = self.ir_manual

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Button("Volver al menu", id="volver-manual-btn", variant="primary")
        yield Container(
            Static(f"Fuente: {self.archivo}", id="manual-file"),
            Horizontal(
                Checkbox("mem2reg", id="pass-mem2reg", value=True),
                Checkbox("instcombine", id="pass-instcombine", value=True),
                Checkbox("simplifycfg", id="pass-simplifycfg", value=True),
                id="manual-passes-row1",
            ),
            Horizontal(
                Checkbox("dce", id="pass-dce", value=False),
                Checkbox("inline", id="pass-inline", value=False),
                Checkbox("loop-unroll", id="pass-loop-unroll", value=False),
                id="manual-passes-row2",
            ),
            Horizontal(
                Checkbox("Linux", id="manual-target-linux", value=True),
                Checkbox("Windows", id="manual-target-windows", value=False),
                id="manual-targets",
            ),
            Horizontal(
                Button("Aplicar Passes", id="manual-aplicar", variant="success"),
                Button("Re-ejecutar IR", id="manual-ejecutar", variant="primary"),
                id="manual-actions",
            ),
            RichLog(id="manual-output", highlight=True, markup=False, auto_scroll=True),
            id="manual-container",
        )
        yield Footer()

    def on_mount(self) -> None:
        self.title = f"IR Manual: {os.path.basename(self.archivo)}"
        self.output = self.query_one("#manual-output", RichLog)
        self.output.write("Panel IR Manual listo.")
        self.output.write("Selecciona passes y presiona 'Aplicar Passes'.")
        self.output.write(f"IR esperado de entrada: {self.ir_base}")
        if not os.path.exists(self.ir_base):
            self.output.write("[AVISO] Aun no existe .ll. Primero compila el archivo.")

    def _passes_seleccionados(self):
        mapping = [
            ("pass-mem2reg", "mem2reg"),
            ("pass-instcombine", "instcombine"),
            ("pass-simplifycfg", "simplifycfg"),
            ("pass-dce", "dce"),
            ("pass-inline", "inline"),
            ("pass-loop-unroll", "loop-unroll"),
        ]
        seleccionados = []
        for checkbox_id, nombre_pass in mapping:
            if self.query_one(f"#{checkbox_id}", Checkbox).value:
                seleccionados.append(nombre_pass)
        return seleccionados

    def _targets_manual_seleccionados(self):
        targets = []
        if self.query_one("#manual-target-linux", Checkbox).value:
            targets.append("linux")
        if self.query_one("#manual-target-windows", Checkbox).value:
            targets.append("windows")
        return targets

    @staticmethod
    def _fmt_ms(segundos):
        try:
            return f"{float(segundos) * 1000.0:.2f} ms"
        except Exception:
            return "n/a"

    def _aplicar_passes(self):
        if not os.path.exists(self.ir_base):
            self.output.write(f"[ERROR] No existe IR base: {self.ir_base}")
            self.notify("Primero compila para generar .ll", severity="error")
            return

        passes = self._passes_seleccionados()
        if not passes:
            self.output.write("[ERROR] No seleccionaste ningun pass.")
            self.notify("Selecciona al menos un pass", severity="warning")
            return

        self.output.write("\n=== IR MANUAL: APLICANDO PASSES ===")
        self.output.write(f"Passes: {', '.join(passes)}")

        try:
            resultado = optimizar_ir_manual_archivo(self.ir_base, self.ir_manual, passes)
        except Exception as e:
            self.output.write(f"[ERROR] {e}")
            self.notify("Fallo aplicando passes", severity="error")
            return

        self.ir_actual = self.ir_manual
        self.output.write(f"Salida IR manual: {resultado['ruta_ir_salida']}")
        self.output.write(
            f"Tiempo optimizacion manual: {self._fmt_ms(resultado.get('tiempo_optimizacion_seg'))}"
        )
        self.output.write(
            f"Instrucciones: {resultado['instrucciones_antes']} -> "
            f"{resultado['instrucciones_despues']} "
            f"({resultado['reduccion_porcentaje']:.2f}%)"
        )
        self.output.write("IR manual optimizado generado.")

    def _re_ejecutar_ir(self):
        ruta_ir = self.ir_actual if os.path.exists(self.ir_actual) else self.ir_base
        if not os.path.exists(ruta_ir):
            self.output.write(f"[ERROR] No hay IR para ejecutar: {ruta_ir}")
            self.notify("No hay IR para ejecutar", severity="error")
            return

        targets = self._targets_manual_seleccionados()
        if not targets:
            self.output.write("[ERROR] Selecciona al menos una plataforma.")
            self.notify("Selecciona Linux y/o Windows", severity="error")
            return

        base_run = os.path.splitext(ruta_ir)[0] + ".manual_run"
        self.output.write("\n=== RE-EJECUCION IR MANUAL ===")
        self.output.write(f"Compilando y ejecutando: {ruta_ir}")
        self.output.write(f"Targets: {', '.join(targets)}")

        try:
            resultado = ejecutar_ir_manual_targets(ruta_ir, base_salida=base_run, targets=targets)
        except Exception as e:
            self.output.write(f"[ERROR] {e}")
            self.notify("Fallo en re-ejecucion IR", severity="error")
            return

        for target, info in resultado.get("targets", {}).items():
            self.output.write(f"\n--- TARGET {target.upper()} ---")
            if not info.get("ok"):
                self.output.write(f"[ERROR] {info.get('error', 'fallo de compilacion')}")
                if info.get("stderr"):
                    self.output.write(f"stderr: {info.get('stderr')}")
                continue

            self.output.write(f"Binario generado: {info.get('binary_path')}")
            self.output.write(
                f"Tiempos: objeto={info.get('tiempo_objeto_ms', 0.0):.2f} ms, "
                f"enlazado={info.get('tiempo_enlazado_ms', 0.0):.2f} ms, "
                f"total={info.get('tiempo_total_generacion_ms', 0.0):.2f} ms"
            )

            if target == "linux":
                if info.get("run_ok"):
                    self.output.write(
                        f"Ejecucion Linux: {info.get('tiempo_ejecucion_ms', 0.0):.2f} ms"
                    )
                    self.output.write("--- SALIDA PROGRAMA ---")
                    salida = info.get("run_stdout", "")
                    if salida.strip():
                        for linea in salida.splitlines():
                            self.output.write(linea)
                    else:
                        self.output.write("(sin salida)")

                    if info.get("run_stderr"):
                        self.output.write("--- STDERR ---")
                        for linea in info["run_stderr"].splitlines():
                            self.output.write(linea)
                else:
                    self.output.write("[ERROR] Fallo ejecutando binario Linux.")
                    if info.get("run_stderr"):
                        self.output.write(f"stderr: {info.get('run_stderr')}")
            elif target == "windows":
                self.output.write(
                    info.get(
                        "run_note",
                        "Ejecucion de .exe omitida en este entorno; validar en Windows real.",
                    )
                )

        if not resultado.get("ok"):
            self.notify("Re-ejecucion con errores", severity="warning")
        else:
            self.notify("Re-ejecucion completada")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "volver-manual-btn":
            self.app.pop_screen()
        elif button_id == "manual-aplicar":
            self._aplicar_passes()
        elif button_id == "manual-ejecutar":
            self._re_ejecutar_ir()


class IRDiffScreen(Screen):
    CSS = """
    #volver-diff-btn { dock: top; margin: 1; width: 22; }
    #diff-container {
        margin: 1;
        border: solid $accent;
        padding: 1 2;
        height: 1fr;
    }
    #diff-files {
        padding: 1;
        background: $panel;
        margin-bottom: 1;
    }
    #diff-legend {
        margin: 0 0 1 0;
        text-style: bold;
        color: $accent;
    }
    #diff-summary {
        margin: 0 0 1 0;
        color: $text;
    }
    #diff-panels {
        height: 1fr;
    }
    #diff-before, #diff-after {
        width: 1fr;
        height: 100%;
        border: solid $primary;
    }
    """

    MODOS = {
        "orig_auto": ("Original vs Automatico", ".ll", ".opt.ll"),
        "orig_manual": ("Original vs Manual", ".ll", ".manual.ll"),
        "auto_manual": ("Automatico vs Manual", ".opt.ll", ".manual.ll"),
    }

    def __init__(self, archivo, modo="orig_manual"):
        super().__init__()
        self.archivo = archivo
        self.base = os.path.splitext(archivo)[0]
        self.modo = modo if modo in self.MODOS else "orig_manual"
        self.titulo_diff, ext_izq, ext_der = self.MODOS[self.modo]
        self.ir_izq = self.base + ext_izq
        self.ir_der = self.base + ext_der

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Button("Volver al menu", id="volver-diff-btn", variant="primary")
        yield Container(
            Static(
                f"Comparacion: {self.titulo_diff}\nIzquierda: {self.ir_izq}\nDerecha: {self.ir_der}",
                id="diff-files",
            ),
            Static(
                "Comparador Diff (paralelo): '=' igual  '~' modificada  '+' agregada  '-' eliminada",
                id="diff-legend",
            ),
            Static("Sin diff calculado", id="diff-summary"),
            Horizontal(
                RichLog(id="diff-before", highlight=False, markup=False, auto_scroll=False),
                RichLog(id="diff-after", highlight=False, markup=False, auto_scroll=False),
                id="diff-panels",
            ),
            id="diff-container",
        )
        yield Footer()

    def on_mount(self) -> None:
        self.title = f"Diff IR: {self.titulo_diff}"
        self.diff_before = self.query_one("#diff-before", RichLog)
        self.diff_after = self.query_one("#diff-after", RichLog)
        self.diff_summary = self.query_one("#diff-summary", Static)
        self._cargar_diff()

    @staticmethod
    def _linea_diff(lado: str, estado: str, numero: int | None, texto: str) -> Text:
        marker = "="
        if estado == "modificada":
            marker = "~"
        elif estado == "agregada":
            marker = "+"
        elif estado == "eliminada":
            marker = "-"

        style = "white"
        if estado == "modificada":
            style = "yellow"
        elif estado == "agregada":
            style = "green" if lado == "despues" else "dim"
        elif estado == "eliminada":
            style = "red" if lado == "antes" else "dim"

        num_txt = f"{numero:>4}" if numero is not None else "    "
        body = texto if texto else "<vacio>"
        linea = Text()
        linea.append(f"{marker} {num_txt} | ", style=f"bold {style}")
        linea.append(body, style=style)
        return linea

    def _pintar_diff_paralelo(self, diff_paralelo):
        self.diff_before.clear()
        self.diff_after.clear()
        self.diff_before.write(Text("IZQUIERDA", style="bold cyan"))
        self.diff_after.write(Text("DERECHA", style="bold cyan"))

        filas = diff_paralelo.get("filas", []) if isinstance(diff_paralelo, dict) else []
        resumen = diff_paralelo.get("resumen", {}) if isinstance(diff_paralelo, dict) else {}

        for fila in filas:
            estado = fila.get("estado", "igual")
            self.diff_before.write(
                self._linea_diff("antes", estado, fila.get("antes_num"), fila.get("antes_texto", ""))
            )
            self.diff_after.write(
                self._linea_diff(
                    "despues", estado, fila.get("despues_num"), fila.get("despues_texto", "")
                )
            )

        self.diff_summary.update(
            "Cambios: "
            f"modificadas={resumen.get('modificadas', 0)}  "
            f"agregadas={resumen.get('agregadas', 0)}  "
            f"eliminadas={resumen.get('eliminadas', 0)}  "
            f"iguales={resumen.get('iguales', 0)}"
        )

    def _cargar_diff(self):
        self.diff_before.clear()
        self.diff_after.clear()
        self.diff_before.write(Text("IZQUIERDA", style="bold cyan"))
        self.diff_after.write(Text("DERECHA", style="bold cyan"))

        if not os.path.exists(self.ir_izq):
            self.diff_before.write(Text(f"No existe: {self.ir_izq}", style="red"))
            self.diff_after.write(Text(f"No existe: {self.ir_izq}", style="red"))
            self.diff_summary.update("Error: falta archivo izquierdo")
            self.notify("Falta archivo izquierdo para comparar", severity="error")
            return

        if not os.path.exists(self.ir_der):
            self.diff_before.write(Text(f"No existe: {self.ir_der}", style="yellow"))
            self.diff_after.write(Text(f"No existe: {self.ir_der}", style="yellow"))
            self.diff_summary.update("Error: falta archivo derecho")
            self.notify("Falta archivo derecho para comparar", severity="warning")
            return

        with open(self.ir_izq, "r", encoding="utf-8") as f:
            ir_izquierda = f.read()
        with open(self.ir_der, "r", encoding="utf-8") as f:
            ir_derecha = f.read()

        self._pintar_diff_paralelo(construir_diff_paralelo(ir_izquierda, ir_derecha))

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "volver-diff-btn":
            self.app.pop_screen()


class MenuScreen(Screen):
    CSS = """
    Screen { align: center middle; }

    #menu-container {
        width: 78;
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
        width: 100%;
        height: auto;
    }

    #botones-row1, #botones-row2, #botones-row3 {
        align: center middle;
        width: 100%;
        height: auto;
    }

    #botones-row2, #botones-row3 {
        margin-top: 1;
    }

    #botones-row1 Button, #botones-row2 Button, #botones-row3 Button {
        margin: 0 1;
        min-width: 15;
    }

    #targets-row {
        margin: 0 0 1 0;
        height: auto;
        align: center middle;
    }

    #targets-row Checkbox {
        margin: 0 2;
        width: auto;
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
            Static("[bold]COMPILADOR PIPELINE[/bold]", id="titulo"),
            Static("Archivo: ninguno", id="file-path"),
            Static("Selecciona un archivo para continuar", id="estado"),
            Container(
                Horizontal(
                    Button("Cargar", id="cargar", variant="primary"),
                    Button("Compilar", id="compilar", variant="success"),
                    Button("IR Manual", id="ir-manual", variant="warning"),
                    id="botones-row1",
                ),
                Horizontal(
                    Button("Orig vs Auto", id="diff-orig-auto", variant="primary"),
                    Button("Orig vs Manual", id="diff-orig-manual", variant="primary"),
                    Button("Auto vs Manual", id="diff-auto-manual", variant="primary"),
                    id="botones-row2",
                ),
                Horizontal(
                    Button("Limpiar Generados", id="limpiar-generados", variant="warning"),
                    Button("Limpiar", id="limpiar", variant="error"),
                    id="botones-row3",
                ),
                id="botones",
            ),
            Horizontal(
                Checkbox("Linux", id="target-linux", value=True),
                Checkbox("Windows", id="target-windows", value=True),
                id="targets-row",
            ),
            Static("Presiona Q o Esc para salir", id="exit-bar"),
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
        elif event.button.id == "ir-manual":
            self.abrir_ir_manual()
        elif event.button.id == "diff-orig-auto":
            self.abrir_diff_ir("orig_auto")
        elif event.button.id == "diff-orig-manual":
            self.abrir_diff_ir("orig_manual")
        elif event.button.id == "diff-auto-manual":
            self.abrir_diff_ir("auto_manual")
        elif event.button.id == "limpiar-generados":
            self.limpiar_generados()
        elif event.button.id == "limpiar":
            self.limpiar()

    def cargar_archivo(self):
        archivo = self.seleccionar_archivo()
        if archivo:
            self.archivo_seleccionado = archivo
            self.query_one("#file-path", Static).update(f"Archivo: {archivo}")
            self.query_one("#estado", Static).update("[green]Archivo cargado[/]")
            self.notify("Archivo cargado")
        else:
            self.notify("No se selecciono archivo", severity="warning")

    def compilar(self):
        if not self.archivo_seleccionado:
            self.query_one("#estado", Static).update("[red]Selecciona un archivo primero[/]")
            self.notify("Selecciona un archivo primero", severity="error")
            return

        targets_fase8 = []
        if self.query_one("#target-linux", Checkbox).value:
            targets_fase8.append("linux")
        if self.query_one("#target-windows", Checkbox).value:
            targets_fase8.append("windows")

        if not targets_fase8:
            self.query_one("#estado", Static).update("[red]Selecciona al menos una plataforma[/]")
            self.notify("Selecciona Linux y/o Windows", severity="error")
            return

        self.app.push_screen(
            CompilacionScreen(
                self.archivo_seleccionado,
                self.run_pipeline,
                tuple(targets_fase8),
            )
        )
        self.query_one("#estado", Static).update("[green]Compilacion finalizada[/]")

    def abrir_ir_manual(self):
        if not self.archivo_seleccionado:
            self.query_one("#estado", Static).update("[red]Selecciona un archivo primero[/]")
            self.notify("Selecciona un archivo primero", severity="error")
            return

        self.app.push_screen(IRManualScreen(self.archivo_seleccionado))

    def abrir_diff_ir(self, modo):
        if not self.archivo_seleccionado:
            self.query_one("#estado", Static).update("[red]Selecciona un archivo primero[/]")
            self.notify("Selecciona un archivo primero", severity="error")
            return

        self.app.push_screen(IRDiffScreen(self.archivo_seleccionado, modo=modo))

    def limpiar(self):
        self.archivo_seleccionado = None
        self.query_one("#file-path", Static).update("Archivo: ninguno")
        self.query_one("#estado", Static).update("Selecciona un archivo para continuar")
        self.notify("Limpiado")

    def limpiar_generados(self):
        resultado = limpiar_artefactos_generados_src("src")
        borrados = len(resultado.get("deleted", []))
        errores = resultado.get("errors", [])

        if errores:
            self.query_one("#estado", Static).update(
                f"[yellow]Limpieza parcial: {borrados} borrados, {len(errores)} errores[/]"
            )
            self.notify("Limpieza parcial (revisa permisos)", severity="warning")
            return

        self.query_one("#estado", Static).update(
            f"[green]Generados limpiados: {borrados} archivos[/]"
        )
        self.notify(f"Se eliminaron {borrados} archivos generados")


class CompiladorApp(App):
    BINDINGS = [
        ("q", "quit", "Salir"),
        ("escape", "quit", "Salir"),
    ]

    def __init__(self, seleccionar_archivo_func, pipeline_func):
        super().__init__()
        self.seleccionar_archivo = seleccionar_archivo_func
        self.run_pipeline = pipeline_func

    def on_mount(self) -> None:
        self.push_screen(MenuScreen(self.seleccionar_archivo, self.run_pipeline))
