import pandas as pd
import random
from faker import Faker

# Configuración
faker = Faker()

# Generar datos ficticios
num_filas = 100  # Puedes ajustar la cantidad de filas según tus necesidades

data = {
    'ID': [i+1 for i in range(num_filas)],
    'Nombre': [faker.first_name() for _ in range(num_filas)],
    'Apellido': [faker.last_name() for _ in range(num_filas)],
    'Edad': [random.randint(18, 65) for _ in range(num_filas)],
    'Genero': [random.choice(['Masculino', 'Femenino', 'Otro']) for _ in range(num_filas)],
    'Ciudad': [faker.city() for _ in range(num_filas)],
    'Pais': [faker.country() for _ in range(num_filas)],
    'Region': [faker.random_element(elements=('Norte', 'Sur', 'Este', 'Oeste')) for _ in range(num_filas)],
    'FechaNacimiento': [faker.date_of_birth(minimum_age=18, maximum_age=65).strftime('%Y-%m-%d') for _ in range(num_filas)],
    'FechaRegistro': [faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S') for _ in range(num_filas)],
    'NivelEducacion': [random.choice(['Primaria', 'Secundaria', 'Universidad', 'Postgrado']) for _ in range(num_filas)],
    'Ocupacion': [faker.job() for _ in range(num_filas)],
    'Ingresos': [round(random.uniform(20000, 80000), 2) for _ in range(num_filas)]
}

# Crear un DataFrame de pandas
df = pd.DataFrame(data)

# Exportar a CSV
df.to_csv('datos_ciudadanos.csv', index=False)

print("Datos generados y exportados correctamente.")
