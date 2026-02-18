class Engine:
    def compute(self, a, op, b):
        if op == "+":
            return a + b
        if op == "-":
            return a - b
        if op == "*":
            return a * b
        if op == "/":
            if b == 0:
                raise ValueError("Division par zéro")
            return a / b
        raise ValueError("Opérateur inconnu")
