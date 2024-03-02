class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def saludar(self):
        print(f"Hola, soy {self.nombre}.")

class Estudiante(Persona):
    def __init__(self, nombre, edad, genero, matricula, carrera):
        super().__init__(nombre, edad, genero)
        self.__matricula = matricula
        self.__carrera = carrera

    def estudiar(self):
        print(f"{self.nombre} está estudiando.")

    # Getter y Setter para matrícula
    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, matricula):
        self.__matricula = matricula

    # Getter y Setter para carrera
    def get_carrera(self):
        return self.__carrera

    def set_carrera(self, carrera):
        self.__carrera = carrera

# Crear un objeto Estudiante
estudiante1 = Estudiante("Jhoan", 20, "Masculino", "2023001", "Analisis de datos")

# Acceder a atributos y métodos
print("Nombre:", estudiante1.nombre)
print("Edad:", estudiante1.edad)
print("Género:", estudiante1.genero)
estudiante1.saludar()
estudiante1.estudiar()

# Acceder a atributos privados usando getters y setters
print("Matrícula:", estudiante1.get_matricula())
print("Carrera:", estudiante1.get_carrera())
estudiante1.set_matricula("2023002")
estudiante1.set_carrera("Ingeniería de Sistemas")
print("Nueva Matrícula:", estudiante1.get_matricula())
print("Nueva Carrera:", estudiante1.get_carrera())
