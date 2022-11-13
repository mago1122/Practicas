class Persona:
    
    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido
    
    def __str__(self) -> str:
        return self.nombre + " " + self.apellido
        