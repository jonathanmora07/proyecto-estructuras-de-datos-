from inspect import stack

class EvaluadorPosfija: 
    def __init__(self): 
        self.pila = stack() 
        self.pilaEvalua = stack() 
        
    def evaluar(self, expresion_posfija): 
        for caracter in expresion_posfija: 
            if caracter.isdigit(): 
                self.pilaEvalua.push(int(caracter)) 
            else: 
                operando2 = self.pilaEvalua.pop() 
                operando1 = self.pilaEvalua.pop() 
                resultado = self.aplicar_operacion(operando1, operando2, caracter) 
                self.pilaEvalua.push(resultado) 
        return self.pilaEvalua.pop()  
    def evaluar_posfija(expresion_posfija, clase_stack): 
        pila = clase_stack() 
        for caracter in expresion_posfija:                           
            if caracter.isdigit():
                pila.push(int(caracter))
        
        
            elif caracter in ('+', '-', '*', '/'):
                operando_b = pila.pop()
                operando_a = pila.pop()
            if operando_a is None or operando_b is None:
                raise ValueError("Expresion posfija mal formada.")
            if caracter == '+':
                resultado = operando_a + operando_b
            elif caracter == '-':
                resultado = operando_a - operando_b
            elif caracter == '*':
                resultado = operando_a * operando_b
            elif caracter == '/':
                if operando_b == 0:
                    raise ZeroDivisionError("División por cero detectada.")
                resultado = operando_a / operando_b
                
            pila.push(resultado)
            resultado_final = pila.pop()
    
        if pila.pop() is not None:
            raise ValueError("Expresion posfija mal formada.")
        
        return resultado_final 