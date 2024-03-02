# Definición de la clase Animal
class Animal:
    def __init__(self, especie, habitat):
        self.especie = especie
        self.habitat = habitat

    def emitir_sonido(self, sonido):
        print(f"El {self.especie} emite el sonido {sonido}.")

# Definición de la clase CuerpoCeleste
class CuerpoCeleste:
    def __init__(self, nombre, tipo, diametro):
        self.nombre = nombre
        self.tipo = tipo
        self.diametro = diametro

    def describir(self):
        print(f"{self.nombre} es un {self.tipo} con un diámetro de {self.diametro} km.")

# Definición de la clase Bebida
class Bebida:
    def __init__(self, nombre, tipo, cantidad_ml):
        self.nombre = nombre
        self.tipo = tipo
        self.cantidad_ml = cantidad_ml

    def servir(self):
        print(f"Sirviendo {self.cantidad_ml} ml de {self.nombre} {self.tipo}.")

# Definición de la clase Texto
class Texto:
    def __init__(self, contenido, idioma):
        self.contenido = contenido
        self.idioma = idioma

    def imprimir(self):
        print(f"Contenido del texto ({self.idioma}): {self.contenido}")

# Definición de la clase Materia
class Materia:
    def __init__(self, nombre, codigo, creditos):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos

    def mostrar_informacion(self):
        print(f"Materia: {self.nombre}, Código: {self.codigo}, Créditos: {self.creditos}")

# Creación de objetos utilizando las clases definidas
animal1 = Animal("León", "Savannah")
cuerpo_celeste1 = CuerpoCeleste("Tierra", "planeta", 12742)
bebida1 = Bebida("Café", "caliente", 250)
texto1 = Texto("Hola mundo!", "Español")
materia1 = Materia("Matemáticas", "MAT101", 4)

# Acceso a los atributos y métodos de los objetos creados
animal1.emitir_sonido("rugido")
cuerpo_celeste1.describir()
bebida1.servir()
texto1.imprimir()
materia1.mostrar_informacion()
