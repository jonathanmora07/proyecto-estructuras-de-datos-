from menus.Banco import MenuBanco
from  menus.menu_lista_enlazada import MenuListaEnlazada
from PyQt5.QtWidgets import QApplication 
from estructuras.lineales.posfija import evaluar_posfija 
from estructuras.lineales.stack import Stack
from PyQt5.QtWidgets import QApplication 
from Banco import Banco 

def main():
    menu = MenuListaEnlazada()
    menu.iniciar() 
   
if __name__ == "__main__":
    main() 
    
from estructuras.lineales.stack import Stack 
    
pruebas = [
        {"posfija": "234*+", "infija_original": "2 + 3 * 4", "esperado": 14},
        {"posfija": "53+2*", "infija_original": "(5 + 3) * 2", "esperado": 16},
        {"posfija": "93/2-", "infija_original": "9 / 3 - 2", "esperado": 1},
        {"posfija": "723*-", "infija_original": "7 - 2 * 3", "esperado": 1}
    ]

print("--- Ejecutando Pruebas de Evaluación Posfija ---")
for i, caso in enumerate(pruebas, 1):
    try:
        res = evaluar_posfija(caso["posfija"], Stack)
        assert res == caso["esperado"], f"Error: se esperaba {caso['esperado']} pero dio {res}"
        print(f"Prueba {i} exitosa: {caso['infija_original']} ({caso['posfija']}) = {res}")
    except Exception as e:
            print(f"Prueba {i} fallida: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiVentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    menu = MenuBanco()
    menu.iniciar()
