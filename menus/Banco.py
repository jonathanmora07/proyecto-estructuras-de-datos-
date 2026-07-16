from Banco import Banco 

class MenuBanco:  
    def __init__(self):
        self.banco = Banco()

    def mostrar_menu(self):
        print("\n--- Menú de Atención Bancaria ---")
        print("1. Agregar cliente")
        print("2. Atender cliente")
        print("3. Mostrar cola")
        print("4. Cerrar banco")
        
def ejecutar_opcion(self, opcion): 
        if opcion == "1": 
            self.banco.agregar_cliente() 
        elif opcion == "2": 
            self.banco.atender_cliente() 
        elif opcion == "3": 
            self.banco.mostrar_clientes()
        elif opcion == "4": 
            # Si el banco se puede cerrar (cola vacía), devuelve True y rompe el ciclo
            return self.banco.intentar_cerrar()
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 4.")
        return False
            
def iniciar(self): 
        while True: 
            self.mostrar_menu() 
            try: 
                opcion = input("Seleccione una opción: ") 
                debe_salir = self.ejecutar_opcion(opcion) 
                if debe_salir: 
                    break 
            except Exception as e: 
                print(f"Ocurrió un error inesperado: {e}") 


