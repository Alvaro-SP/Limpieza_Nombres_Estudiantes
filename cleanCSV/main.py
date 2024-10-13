import csv
import re

# Archivo de entrada y salida
input_file = 'becadosactivos.csv'
output_file = 'archivo_salida2.csv'

# Función para limpiar espacios extra
def clean_text(text):
    # Eliminar espacios al inicio y al final, y reducir múltiples espacios a uno solo
    return ' '.join(text.split())

# Función para extraer las fechas y el monto del texto de la columna TIEMPO_DE_LA_BECA
def extract_values(text):
    # Buscar la fecha de inicio (formato: día-mes)
    inicio_match = re.search(r'\b\d{1,2}-[A-Za-z]+\b', text)
    fecha_inicio = inicio_match.group(0) if inicio_match else ''

    # Buscar la fecha de fin (formato: día-mes-año)
    fin_match = re.search(r'\b\d{1,2}-[A-Za-z]+-\d{4}\b', text)
    fecha_fin = fin_match.group(0) if fin_match else ''

    # Buscar el monto (último número en el texto)
    monto_match = re.search(r'\d+$', text)
    monto = monto_match.group(0) if monto_match else ''

    return fecha_inicio, fecha_fin, monto

# Leer el archivo CSV y procesar el contenido
with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
     open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
    
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    # Leer la primera fila (cabecera)
    headers = next(reader)
    # Añadir las nuevas columnas
    headers.extend(['Fecha Inicio', 'Fecha Fin', 'Monto'])
    writer.writerow(headers)
    
    for row in reader:
        # Limpiar cada celda del archivo CSV
        cleaned_row = [clean_text(cell) for cell in row]
        
        # Suponiendo que la columna 'TIEMPO_DE_LA_BECA' está en la primera posición (índice 0)
        tiempo_beca = cleaned_row[8]
        
        # Extraer los valores de fecha de inicio, fecha de fin y monto
        fecha_inicio, fecha_fin, monto = extract_values(tiempo_beca)
        
        # Añadir los valores extraídos a la fila actual
        cleaned_row.extend([fecha_inicio, fecha_fin, monto])
        
        # Escribir la fila procesada en el archivo de salida
        writer.writerow(cleaned_row)

print(f"Archivo procesado correctamente y guardado como {output_file}.")