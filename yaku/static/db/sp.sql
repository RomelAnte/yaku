/*DELIMITER //
CREATE PROCEDURE promedio_consumo_mensual()
BEGIN
SELECT l.mes_lec, l.anio_lec, AVG(l.lectura_actual_lec - l.lectura_anterior_lec) AS promedio_consumo 
FROM lectura l 
INNER JOIN detalle d ON d.fk_id_lec = l.id_lec 
GROUP BY l.mes_lec, l.anio_lec 
ORDER BY 
    l.anio_lec,  -- Primero ordena por año
    CASE l.mes_lec 
        WHEN 'Enero' THEN 1 
        WHEN 'Febrero' THEN 2 
        WHEN 'Marzo' THEN 3 
        WHEN 'Abril' THEN 4 
        WHEN 'Mayo' THEN 5 
        WHEN 'Junio' THEN 6 
        WHEN 'Julio' THEN 7 
        WHEN 'Agosto' THEN 8 
        WHEN 'Septiembre' THEN 9 
        WHEN 'Octubre' THEN 10 
        WHEN 'Noviembre' THEN 11 
        WHEN 'Diciembre' THEN 12 
    END;  -- Luego ordena por mes
END //
DELIMITER ;*/

DELIMITER //
CREATE PROCEDURE estado_consumo_mensual()
BEGIN

Select lectura.estado_lec, count(lectura.estado_lec) as cantidad from lectura
where lectura.mes_lec = 'Enero' and lectura.anio_lec = 2024
group by lectura.estado_lec


