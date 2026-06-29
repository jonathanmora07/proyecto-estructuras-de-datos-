import sys
import importlib

qt_modules = ["PyQt5.QtWidgets", "PyQt6.QtWidgets", "PySide6.QtWidgets"]
QtWidgets = None
for module_name in qt_modules:
    try:
        QtWidgets = importlib.import_module(module_name)
        break
    except ImportError:
        pass

if QtWidgets is None:
    raise ImportError("No supported Qt binding found. Install PyQt5, PyQt6 or PySide6.")

QApplication = QtWidgets.QApplication
QMainWindow = QtWidgets.QMainWindow
QPushButton = QtWidgets.QPushButton
QVBoxLayout = QtWidgets.QVBoxLayout
QWidget = QtWidgets.QWidget
QLabel = QtWidgets.QLabel
QMenu = QtWidgets.QMenu
QAction = QtWidgets.QAction

from menus.menu_lista_enlazada import MenuListaEnlazada

class MiVentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        # 1. Configuración de la Ventana Principal (QMainWindow)
        self.setWindowTitle("Ejemplo de Qt Designer en Código")
        self.resize(600, 400)

        # 2. Configuración del Contenedor Central (QWidget)
        # Nota: QMainWindow obligatoriamente necesita un widget central.
        self.widget_central = QWidget()
        self.setCentralWidget(self.widget_central)

        # Diseño básico para el interior de la ventana
        layout = QVBoxLayout()
        self.label_estado = QLabel("Selecciona una opción del menú", self)
        layout.addWidget(self.label_estado)
        self.widget_central.setLayout(layout)

        # 3. Inicializar la Barra de Menús (QMenuBar)
        self.barra_menus = self.menuBar()

        # 4. Crear el Menú Principal (QMenu)
        self.menu_archivo = QMenu("Archivo", self)
        self.barra_menus.addMenu(self.menu_archivo)

        # 5. Crear las Acciones (QAction) y añadirlas al Menú
        # Acción 1
        self.accion_nuevo = QAction("Nuevo", self)
        self.accion_nuevo.triggered.connect(lambda: self.mostrar_mensaje("Has hecho clic en 'Nuevo'"))
        self.menu_archivo.addAction(self.accion_nuevo)

        # Acción 2
        self.accion_abrir = QAction("Abrir", self)
        self.accion_abrir.triggered.connect(lambda: self.mostrar_mensaje("Has hecho clic en 'Abrir'"))
        self.menu_archivo.addAction(self.accion_abrir)

        # Separador visual en el menú (opcional pero recomendado)
        self.menu_archivo.addSeparator()

        # Acción 3
        self.accion_salir = QAction("Salir", self)
        self.accion_salir.triggered.connect(self.close) # Cierra la aplicación
        self.menu_archivo.addAction(self.accion_salir)

    def mostrar_mensaje(self, texto):
        """Función auxiliar para ver el comportamiento de las acciones."""
        self.label_estado.setText(texto)


# Ejecución de la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiVentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
