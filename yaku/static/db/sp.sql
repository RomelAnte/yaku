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
DELIMITER ;

DELIMITER //
CREATE PROCEDURE estado_lectura()
BEGIN

	Select lectura.estado_lec, count(lectura.estado_lec) as cantidad from lectura
	where lectura.mes_lec = 'Enero' and lectura.anio_lec = 2024
	group by lectura.estado_lec;
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE total_consumo_mensual()
BEGIN
	SELECT c.mes_consumo  AS mes, c.anio_consumo as anio, (sum(l.lectura_actual_lec) - sum(l.lectura_anterior_lec)) AS total_consumos
	FROM consumo c
	INNER join lectura l 
	on c.id_consumo = l.fk_id_consumo 
	GROUP BY mes, anio
	ORDER by anio,
	    CASE mes 
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
DELIMITER ;

-- Total de eventos por tipo
DELIMITER //
CREATE PROCEDURE total_eventos_tipo()
BEGIN
	select te.nombre_te, count(e.fk_id_te) NumeroEventos from tipo_evento te 
	inner join evento e 
	on te.id_te = e.fk_id_te 
	group by(te.nombre_te);
END //
DELIMITER ;

-- Total de socios por su tipo
DELIMITER //
CREATE PROCEDURE total_socios_tipo()
BEGIN
	select tipo_soc, count(tipo_soc) as Tipo from socio  
	group by tipo_soc;
END //
DELIMITER ;


-- Cantidad de medidores en uso comparado con los no asignados
DELIMITER $$  
CREATE PROCEDURE sp_porcentaje_medidores_uso()  
BEGIN  
	SELECT  
        (SELECT COUNT(*) FROM medidor WHERE estado_med = 'ACTIVO') AS medidores_en_uso,  
        (SELECT COUNT(*) FROM medidor WHERE estado_med = 'INACTIVO') AS medidores_inactivos; 
END $$  
DELIMITER ;*/

-- Numero de socios asistentes a los eventos
DELIMITER $$  
CREATE PROCEDURE sp_total_asistentes_eventos()  
BEGIN  
	select te.nombre_te, count(a.fk_id_soc) as TotalSocios, e.fecha_hora_eve from asistencia a 
	inner join evento e 
	on a.fk_id_eve = e.id_eve 
	inner join tipo_evento te 
	on te.id_te = e.fk_id_te 
	where a.tipo_asi <> 'FALTA' and a.tipo_asi <> 'REPRESENTANTE'
	group by e.id_eve;
END $$  
DELIMITER ;
