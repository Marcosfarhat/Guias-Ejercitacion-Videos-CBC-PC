import pandas as pd

# Datos para datos1.csv
datos1 = {
    'First Name': ['Luciana', 'Julián', 'Mariano', 'Rogelio', 'Andrea'],
    'Last Name': ['Juárez', 'Manzur', 'Álvarez', 'Linares', 'Gómez'],
    'Location': ['Santiago del Estero', 'Santiago del Estero', 'San Luis', 'Mendoza', 'CABA'],
    'Value': [95, 88, 90, 83, 92]
}

# Datos para datos2.csv
datos2 = {
    'First Name': ['Jazmín', 'Ana Laura', 'Roberto', 'Joaquín', 'Antonio', 'Marcos', 'Nicolás', 'Agustín'],
    'Last Name': ['Gerez', 'Jiménez', 'Luna', 'Ortiz', 'Peñate', 'Medina', 'Villalba', 'Méndez'],
    'Location': ['Formosa', 'Chaco', 'Corrientes', 'Misiones', 'Río Negro', 'Santa Cruz', 'Santa Cruz', 'Formosa'],
    'Value': [93, 86, 88, 84, 83, 80, 79, 77]
}

# Datos para datos3.csv
datos3 = {
    'First Name': ['Andrés', 'Pablo', 'Pablo', 'Paulina', 'Paulina', 'Rosana', 'Victoria'],
    'Last Name': ['Gil Gómez', 'Raza', 'Paz Iraola', 'Estévez', 'Roldán', 'Olmos', 'Antón'],
    'Location': ['CABA', 'Buenos Aires', 'Aires', 'La Pampa', 'CABA', 'Córdoba', 'Salta'],
    'Value': [90, 89, 88, 86, 84, 80, 62]
}

# Crear DataFrames
df1 = pd.DataFrame(datos1)
df2 = pd.DataFrame(datos2)
df3 = pd.DataFrame(datos3)

# Guardar como CSV
df1.to_csv('datos1.csv', index=False)
df2.to_csv('datos2.csv', index=False)
df3.to_csv('datos3.csv', index=False)