import os

input_file = 'Estados.txt'
output_file = 'resultado.txt'

try:
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        lineas = f_in.readlines()
        datos = lineas[1:] 
        
        f_out.write("Reporte de Análisis por Estado\n")
        f_out.write("=" * 50 + "\n")
        
        for linea in datos:
            valores = linea.strip().split(',')
            if len(valores) == 7:
                estado = valores[0]
                temp = valores[1]
                humedad = valores[2]
                costo_alojamiento = int(valores[3])
                costo_transporte = int(valores[4])
                
                costo_total = costo_alojamiento + costo_transporte
                
                f_out.write(f"Estado: {estado} | Temp: {temp}°C | Humedad: {humedad}% | Costo Total (Alojamiento + Transporte): ${costo_total}\n")
                
        f_out.write("=" * 50 + "\n")
        f_out.write(f"Total de estados procesados: {len(datos)}\n")

except Exception as e:
    print(f"Error procesando los datos: {e}")