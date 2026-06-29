class InfixToPostfixConverter:
    def __init__(self, stack_instance):
        # Recibe e integra la clase Stack existente sin modificarla
        self.stack = stack_instance
        # Definimos la precedencia de los operadores (incluyendo $ para potencia)
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '$': 3}

    def _is_operator(self, char):
        return char in self.precedence

    def convert(self, expression: str) -> str:
        postfix = []
        # Aseguramos que la pila esté vacía antes de iniciar
        while not self.stack.is_empty():
            self.stack.pop()

        # Procesamos la expresión carácter por carácter
        for char in expression:
            # Si es un operando (letra o número), se va directo al resultado
            if char.isalnum():
                postfix.append(char)
            
            # Si es un paréntesis de apertura, se empuja a la pila
            elif char == '(':
                self.stack.push(char)
            
            # Si es un paréntesis de cierre, desapilamos hasta encontrar el de apertura
            elif char == ')':
                while not self.stack.is_empty() and self.stack.peek() != '(':
                    postfix.append(self.stack.pop())
                self.stack.pop()  # Elimina el '(' de la pila
            
            # Si es un operador
            elif self._is_operator(char):
                while (not self.stack.is_empty() and 
                       self.stack.peek() != '(' and 
                       self.precedence.get(self.stack.peek(), 0) >= self.precedence[char]):
                    postfix.append(self.stack.pop())
                self.stack.push(char)

        # Vaciamos los operadores restantes en la pila
        while not self.stack.is_empty():
            postfix.append(self.stack.pop())

        return "".join(postfix)