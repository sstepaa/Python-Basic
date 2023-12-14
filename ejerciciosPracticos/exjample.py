def carga(vec1, vec2):
    num_curso = int(input('Ingresa el número del curso (1-5): '))
    
    while num_curso < 1 or num_curso > 5:
        num_curso = int(input('Error - Ingresa un número de curso válido (1-5): '))
    
    # Iterar sobre los cursos en vec1
    for i in range(len(vec1)):
        if vec1[i] == num_curso:
            num_presentes = int(input(f'Ingresa el número de estudiantes presentes en el curso {num_curso}: '))
            vec2.append(num_presentes)

# Ejemplo de uso
vec_cursos = [1, 2, 3, 4, 5]
vec_cursos_presentes = []  # Inicializar el vector de presentes

# Llamar a la función carga
carga(vec_cursos, vec_cursos_presentes)

# Imprimir el resultado
print(f'Presentes por curso: {vec_cursos_presentes}')