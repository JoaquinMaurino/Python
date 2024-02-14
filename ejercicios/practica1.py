# Promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

# diferencias de duracion
diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max = round(100 - dalto_curso / otros_cursos_max * 100, 1)
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

print("-----------------------------------------")
print(f"el curso de dalto dura un {diferencia_con_min}% menos que el mas rapido")
print(f"el curso de dalto dura un {diferencia_con_max}% menos que el mas largo")
print(f"el curso de dalto dura un {diferencia_con_promedio}% menos que el promedio")
print("-----------------------------------------")

# duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5

# calculando porcentaje de tiempo vacio removido
tiempo_vacio_promedio = 100 - otros_cursos_promedio / crudo_promedio * 100
tiempo_vacio_dalto = round(100 - dalto_curso / crudo_dalto * 100, 1)

# mostrando la cantidad de tiempo vacio que se remueven
print(f"el curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio")
print(f"el curso de dalto elimina un {tiempo_vacio_dalto}% de tiempo vacio")

print("-----------------------------------------")
# mostrando diferencias si los cursos duraran 10hs
print(
    f"Ver 10 hs de este curso equivale a ver {round(10 * otros_cursos_promedio / dalto_curso, 1)}hs de otros cursos"
)
print(
    f"Ver 10 hs de otro curso equivale a ver {round(10 * dalto_curso / otros_cursos_promedio, 1)}hs de este curso"
)
print("-----------------------------------------")
