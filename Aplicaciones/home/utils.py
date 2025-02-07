from django.db import connection
from decimal import Decimal

def promedio_consumo():
    with connection.cursor() as cursor:
        cursor.callproc('promedio_consumo_mensual')
        result = cursor.fetchall()
    
    # Asegúrate de que result no esté vacío
    if not result:
        return []

    return [
        {
            'mes': row[0],  # 'JULIO'
            'anio': row[1],  # 2023
            'promedio': row[2]  # Decimal('-19.738007') convertido a float
        }
        for row in result
    ]
    
def estado_lectura():
    with connection.cursor() as cursor:
        cursor.callproc('estado_lectura')
        result = cursor.fetchall()
    
    # Asegúrate de que result no esté vacío
    if not result:
        return []

    return [
        {
            'estado_lec': row[0],  # 'JULIO'
            'cantidad': row[1],  # 2023
        }
        for row in result
    ]
    
def total_consumo_mensual():
    with connection.cursor() as cursor:
        cursor.callproc('total_consumo_mensual')
        result = cursor.fetchall()
    
    # Asegúrate de que result no esté vacío
    if not result:
        return []

    return [
        {
            'mes': row[0],  
            'anio': row[1],  
            'total_consumos': row[1],  
        }
        for row in result
    ]