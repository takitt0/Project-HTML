class Perro:
    def __init__(self, nombre):
        self.nombre = nombre
        self.action = "Woof!"

    def action(self):
        print(self.action)

class Gato:
    def __init__(self, nombre):
        self.nombre = nombre
        self.action = "Mauyar!"

    def actionn(self):
        print(self.action)
        
sumar = lambda x,y : x + y
restar = lambda x,y : x - y
mul = lambda x,y : x ** y

print(f"2+2 es {sumar(2, 2)}")
