import csv

# Archivo de entrada y salida
input_file = 'becadosactivos.csv'
output_file = 'archivo_salida.csv'

# Función para limpiar espacios extra
def clean_text(text):
    # Eliminar espacios al inicio y al final, y reducir múltiples espacios a uno solo
    return ' '.join(text.split())

# Leer el archivo CSV y limpiar los textos
with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
     open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
    
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    for row in reader:
        # Limpiar cada celda del archivo CSV
        cleaned_row = [clean_text(cell) for cell in row]
        writer.writerow(cleaned_row)

print(f"Archivo procesado correctamente y guardado como {output_file}.")
