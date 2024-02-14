# falto el profe y los alumnos van a dar la clase
# el mayor es el profesor y el menor el asistente


# funcion para ingresar nombre y edad de los alumnos:
def get_students(quantity):
    students = []
    for i in range(quantity):
        name = input("Student name: ")
        age = int(input("Student age: "))
        student = (name, age)
        students.append(student)
    # Ordeno el array de estudiantes por su edad
    students.sort(key=lambda x: x[1])
    asistente = students[
        0
    ]  # accedo al primer elemento del array osea el alumno mas chico
    profesor = students[
        -1
    ]  # accedo al ultimo elemento del array osea el alumno mas grande
    return asistente, profesor


asistente, profesor = get_students(4)

print(
    f""" El profesor es {profesor[0]} y su edad es: {profesor[1]}.
Su asistente es {asistente[0]} y su edad es: {asistente[1]}"""
)
