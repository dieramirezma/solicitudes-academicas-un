USE solicitudes_consejo;
DROP PROCEDURE IF EXISTS verificar_estudiante;
DROP PROCEDURE IF EXISTS estudiante_crear_solicitud;
DROP PROCEDURE IF EXISTS solicitudes;
DROP PROCEDURE IF EXISTS solicitud_carrera;
DROP PROCEDURE IF EXISTS solicitud_sede;
DROP PROCEDURE IF EXISTS obtener_datos;
DROP PROCEDURE IF EXISTS update_estudiante;
DROP PROCEDURE IF EXISTS sede_pasar_csu;
DROP PROCEDURE IF EXISTS carrera_pasar_facultad;
DROP PROCEDURE IF EXISTS update_estado;
DROP PROCEDURE IF EXISTS estudiante_ver_solicitud;
DROP PROCEDURE IF EXISTS cedula_estudiante;

DELIMITER $$
CREATE PROCEDURE obtener_datos(IN cedula INT, OUT conId INT, OUT carId INT, OUT facId INT)
BEGIN
	  SET conId = 0;
      SET carId = 0;
      SET facId = 0;
	  IF EXISTS (SELECT 1 FROM estudiapregrado WHERE perCedulaEst = cedula)THEN
        SELECT carSNIESPregrado INTO carId
        FROM estudiapregrado
        WHERE perCedulaEst = cedula;

		SELECT facultad_facId INTO facId  
        FROM carrera
        WHERE carSNIES = carId;
        
        SELECT conId INTO conId  
        FROM carreracon
        WHERE carSNIES = carId;
        
    ELSEIF EXISTS(SELECT 1 FROM estudiaposgrado WHERE perCedulaEst = cedula)THEN
        SELECT carSNIESPosgrado INTO carId
        FROM estudiaposgrado
        WHERE perCedulaEst = cedula;

        SELECT facultad_facId INTO facId  
        FROM carrera
        WHERE carSNIES = carId;
        
        SELECT conId INTO conId  
        FROM carreracon
        WHERE carSNIES = carId;
        END IF;
END $$
DELIMITER;

DELIMITER $$
CREATE PROCEDURE verificar_estudiante(IN cedulaEstudiante INT, OUT nivel VARCHAR(30))
BEGIN
    IF EXISTS (SELECT 1 FROM pregradoest WHERE perCedulaEst = cedulaEstudiante)
    THEN SET nivel = 'Pregrado';
    ELSEIF EXISTS(SELECT 1 FROM posgradoest WHERE perCedulaEst = cedulaEstudiante)
    THEN SET nivel = 'Posgrado';
    ELSE
    SET nivel = '0';
    END IF;
END $$
DELIMITER;

DELIMITER $$
CREATE PROCEDURE solicitudes(
    IN cedulaEstudiante INT,
    IN iDNomSolicitud INT,
    IN medio VARCHAR(45),
    IN tipo VARCHAR(45),
    IN comentarios LONGTEXT,
    OUT lastSolicitud INT
)
BEGIN
    DECLARE ultimaSolId INT;

    START TRANSACTION;

    INSERT INTO solicitud (nomId, solMedio, solTipo, solFechaEnvio, solComentarios, solEstado)
        VALUES (iDNomSolicitud, medio, tipo, CURRENT_DATE(), comentarios, 'Sin resolver');

    SET ultimaSolId = LAST_INSERT_ID();
	UPDATE variable_solicitudes SET var_sol = @ultimaSolId;
    INSERT INTO estudiante_has_solicitud (perCedulaEstudiante, solId)
        VALUES (cedulaEstudiante, ultimaSolId);

    SET lastSolicitud = ultimaSolId;

    COMMIT;
END $$
DELIMITER ;


DELIMITER $$
CREATE PROCEDURE solicitud_carrera(
	IN cedulaEstudiante INT,
    IN lastSolId INT,
    IN iDNomSolicitud INT, 
    IN solTipo varchar(45)
)
BEGIN
		CALL  obtener_datos(cedulaEstudiante, @conId, @carId, @facId);
        INSERT INTO carrerasolicitud (solId, nomId, conIdCarrera, carSNIES , facId, carsolTipo)
		VALUES (lastSolId,iDNomSolicitud, @conId, @carId, @facId, solTipo);
END $$
DELIMITER;

DELIMITER $$
CREATE PROCEDURE solicitud_sede(
	IN cedulaEstudiante INT,
    IN lastSolId INT,
    IN iDNomSolicitud INT
)
BEGIN
		CALL  obtener_datos(cedulaEstudiante, @conId, @carId, @facId);
        INSERT INTO sedesolicitud(solId, nomId, conId)
		VALUES (lastSolId,iDNomSolicitud, @conId);
END $$
DELIMITER;

DELIMITER $$
CREATE PROCEDURE estudiante_crear_solicitud(
    IN cedulaEstudiante INT,
    IN iDNomSolicitud INT,
    IN medio varchar(45),
    IN comentarios LONGTEXT
)
BEGIN
	SET FOREIGN_KEY_CHECKS=0;
    CALL verificar_estudiante(cedulaEstudiante, @nivel);
    CASE @nivel
    WHEN 'Pregrado' THEN
        IF(iDNomSolicitud>0 AND iDNomSolicitud<21)THEN 
        
        CALL solicitudes(cedulaEstudiante, iDNomSolicitud, medio, 'Carrera' ,comentarios, @ultimaSolId);
        CALL solicitud_carrera(cedulaEstudiante, @ultimaSolId, iDNomSolicitud, 'Solicitud de pregrado');

        ELSEIF(iDNomSolicitud>26 AND iDNomSolicitud<37)THEN 
        
        CALL solicitudes(cedulaEstudiante, iDNomSolicitud, medio, 'Sede' ,comentarios, @ultimaSolId);
        CALL solicitud_sede(cedulaEstudiante, @ultimaSolId, iDNomSolicitud);
        
        ELSE select'Solicitud no permitida';
        END IF;
    WHEN 'Posgrado' THEN
		IF(iDNomSolicitud>0 AND iDNomSolicitud<23)THEN 
        
		CALL solicitudes(cedulaEstudiante, iDNomSolicitud, medio, 'Carrera' ,comentarios, @ultimaSolId);
        CALL solicitud_carrera(cedulaEstudiante, @ultimaSolId, iDNomSolicitud, 'Solicitud de posgrado');
        
        ELSEIF(iDNomSolicitud>22 AND iDNomSolicitud<27)THEN
        
		CALL solicitudes(cedulaEstudiante, iDNomSolicitud, medio, 'Carrera' ,comentarios, @ultimaSolId);
        CALL solicitud_carrera(cedulaEstudiante, @ultimaSolId, iDNomSolicitud, 'Solicitud por comite posgrado');
        
		ELSEIF(iDNomSolicitud>26 AND iDNomSolicitud<37)THEN
        
		 CALL solicitudes(cedulaEstudiante, iDNomSolicitud, medio, 'Sede' ,comentarios, @ultimaSolId);
        CALL solicitud_sede(cedulaEstudiante, @ultimaSolId, iDNomSolicitud);
        
        ELSE select'Solicitud no permitida';
        END IF;
    ELSE
        SELECT 'No se encontro un estudiante con esa cedula.';
END CASE;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE update_estudiante(
  IN cedulaEstudiante INT,
  IN solicitudID INT,
  IN comentariosNuevos longtext
)
BEGIN
	UPDATE solicitud AS s
    INNER JOIN estudiante_has_solicitud AS es ON s.solId = es.solId
    SET s.solComentarios = comentariosNuevos
    WHERE es.perCedulaEstudiante = cedulaEstudiante AND s.solId = solicitudID;
END $$
DELIMITER ;

drop procedure if exists update_estado;
DELIMITER $$
CREATE PROCEDURE update_estado(
  IN solicitudID INT,
  IN nuevoEstado VARCHAR(30)
)
BEGIN
	UPDATE solicitud SET solEstado = nuevoEstado WHERE solId = solicitudID;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE carrera_pasar_facultad(
  IN cedulaEstudiante INT,
  IN solicitudID INT
)
BEGIN
	CALL obtener_datos(cedulaEstudiante, @conId, @nomId, @facId);
	SELECT nomId INTO @nomId
        FROM solicitud
        WHERE solId = solicitudID;
	
     INSERT INTO facultadsolicitud(solId, nomId, conId)
		VALUES (solicitudID,@nomId, @conId);
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE sede_pasar_csu(
  IN cedulaEstudiante INT,
  IN solicitudID INT
)
BEGIN
	CALL obtener_datos(cedulaEstudiante, @conId, @nomId, @facId);
	SELECT nomId INTO @nomId
        FROM solicitud
        WHERE solId = solicitudID;
	
     INSERT INTO csusolicitud(solId, nomId, conId)
		VALUES (solicitudID,@nomId, @conId);
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE estudiante_ver_solicitud(
  IN cedulaEstudiante INT
)
BEGIN
    IF EXISTS (SELECT * FROM estudiante WHERE EXISTS(
		SELECT 1 FROM estudiante WHERE perCedula = cedulaEstudiante) 
		AND NOT EXISTS(SELECT 1 FROM egresado WHERE perCedulaEst = cedulaEstudiante))THEN
		SELECT * FROM vw_estudiante_solicitudes WHERE cedulaEstudiante = perCedulaEstudiante;
     ELSE
     SELECT 'No se encontro un estudiante con esta cedula';
     END IF;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE cedula_estudiante(
  IN usuari0 varchar(60)
)
BEGIN
	SELECT cedula FROM cedulas WHERE usuario = usuari0;
END $$
DELIMITER ;


DELIMITER $$
CREATE TRIGGER validar_nomId
BEFORE INSERT ON solicitud
FOR EACH ROW
BEGIN
    DECLARE numId INT;
    SET numId = NEW.nomId;
    
    IF NOT numId REGEXP '^[0-9]+$' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El valor de nomId debe ser numérico';
    END IF;
END$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER validar_solMedio
BEFORE INSERT ON solicitud
FOR EACH ROW
BEGIN
    DECLARE medio VARCHAR(45);
    SET medio = NEW.solMedio;
    
    IF NOT (medio = 'SIA' OR medio = 'Formulario') THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El valor de solMedio debe ser "SIA" o "Formulario"';
    END IF;
END$$
DELIMITER ;

DROP TRIGGER IF EXISTS validar_solTipo;
DELIMITER $$
CREATE TRIGGER validar_solTipo
BEFORE INSERT ON solicitud
FOR EACH ROW
BEGIN
    DECLARE tipo VARCHAR(45);
    SET tipo = NEW.solTipo;
    
    IF NOT (tipo = 'facultad' OR tipo = 'sede' OR tipo = 'csu') THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El valor de solTipo debe ser "facultad", "sede" o "csu"';
    END IF;
END$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER validar_estudiante_has_solicitud	
BEFORE INSERT ON estudiante_has_solicitud
FOR EACH ROW
BEGIN
    DECLARE cedulaExist INT;
    DECLARE solExist INT;
    
    SET cedulaExist = (SELECT COUNT(*) FROM estudiante WHERE perCedula = NEW.perCedulaEstudiante);
    SET solExist = (SELECT COUNT(*) FROM solicitud WHERE solId = NEW.solId);
    
    IF cedulaExist = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El valor de perCedulaEstudiante no existe en la tabla estudiante';
    END IF;
    
    IF solExist = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El valor de solId no existe en la tabla solicitud';
    END IF;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE update_estudiante(
  IN cedulaEstudiante INT,
  IN solicitudID INT,
  IN comentariosNuevos longtext
)
BEGIN
	UPDATE solicitud AS s
    INNER JOIN estudiante_has_solicitud AS es ON s.solId = es.solId
    SET s.solComentarios = comentariosNuevos
    WHERE es.perCedulaEstudiante = cedulaEstudiante AND s.solId = solicitudID;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE update_estado(
  IN solicitudID INT
)
BEGIN
	UPDATE solicitud SET solEstado = 'Resuelta' WHERE solId = solicitudID;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE carrera_pasar_facultad(
  IN cedulaEstudiante INT,
  IN solicitudID INT
)
BEGIN
    DECLARE conId INT;
    DECLARE nomId INT;
    DECLARE facId INT;

    
    START TRANSACTION;

    SELECT perCedulaEstudiante INTO cedulaEstudiante FROM estudiante_has_solicitud WHERE solId = solicitudID;

    CALL obtener_datos(cedulaEstudiante, @conId, @nomId, @facId);
    SELECT @nomId INTO nomId;

    INSERT INTO facultadsolicitud(solId, nomId, conId)
        VALUES (solicitudID, nomId, @conId);

    COMMIT;
END $$
DELIMITER ;


DELIMITER $$
CREATE PROCEDURE sede_pasar_csu(
  IN cedulaEstudiante INT,
  IN solicitudID INT
)
BEGIN
	CALL obtener_datos(cedulaEstudiante, @conId, @nomId, @facId);
	SELECT nomId INTO @nomId
        FROM solicitud
        WHERE solId = solicitudID;
	
     INSERT INTO csusolicitud(solId, nomId, conId)
		VALUES (solicitudID,@nomId, @conId);
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE cedula_estudiante(
  IN usuari0 varchar(60)
)
BEGIN
	SELECT cedula FROM cedulas WHERE usuario = usuari0;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE solicitudes_nombres()
BEGIN
	SELECT * FROM nombresSolicitudes;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE solicitudes_requisitos(
  IN nombre INT
)
BEGIN
	SELECT nomId, reqId, reqNombre FROM solicitudes_has_requisitos NATURAL JOIN requisitosNombres WHERE nomId = nombre;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE vista_del_comite()
BEGIN
	SELECT * FROM vw_comite_vista;
END $$
DELIMITER ;

drop procedure if exists miembros_del_comite;
DELIMITER $$
CREATE PROCEDURE miembros_del_comite(IN comIdEn int)
BEGIN
	SELECT perNombres, miemRol, comMiemFechaInicio FROM
    miembro_comite NATURAL JOIN persona 
    WHERE comId = comIdEn;
END $$
DELIMITER ;
drop table if exists variable_solicitudes;
CREATE TABLE variable_solicitudes (
    var_sol INT
);
insert into variable_solicitudes values (65);









call miembros_del_comite(2);
CALL estudiante_ver_solicitud(541918572);
CALL vista_del_comite();