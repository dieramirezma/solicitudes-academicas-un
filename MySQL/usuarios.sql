USE solicitudes_consejo;

drop table if exists cedulas;
create table cedulas (usuario varchar(100), cedula int key);
insert into cedulas values ('fvalderramab', '784275110');
insert into cedulas values ('dieramirezma', '541918572');
insert into cedulas values ('axgomezm', '919584433');
insert into cedulas values ('bforerob', '126955156');
insert into cedulas values ('glondonot', '827389691');
insert into cedulas values ('antoniop', '638952303');
insert into cedulas values ('josep', '186678884');
insert into cedulas values ('manuelp', '523130863');
insert into cedulas values ('franciscop', '774499582');
insert into cedulas values ('davidp', '413220262');
insert into cedulas values ('juanp', '867165460');
insert into cedulas values ('josuep', '211429035');
insert into cedulas values ('javierp', '499098560');
insert into cedulas values ('danielp', '172112547');
insert into cedulas values ('luisp', '216686401');
insert into cedulas values ('isabellap', '909068105');

insert into cedulas values ('oliviap', '56417558');
insert into cedulas values ('alexisp', '802182666');
insert into cedulas values ('sofiap', '652830979');
insert into cedulas values ('victoriap', '812766896');
insert into cedulas values ('ameliap', '904769687');
insert into cedulas values ('alexap', '341582364');
insert into cedulas values ('juliap', '98021231');
insert into cedulas values ('julianp', '230951818');
insert into cedulas values ('julianap', '582701184');
insert into cedulas values ('camilap', '569319906');
insert into cedulas values ('alexandrap', '381135508');
insert into cedulas values ('garciap', '954182797');
insert into cedulas values ('gonzalezp', '967252737');
insert into cedulas values ('rodriguezp', '703317196');
insert into cedulas values ('fernandezp', '817595237');
insert into cedulas values ('lopezp', '135931789');

DROP USER IF EXISTS 'estudianteX'@'localhost';
DROP USER IF EXISTS 'admin1'@'localhost';
DROP USER IF EXISTS 'comite_sede'@'localhost';

DROP ROLE IF EXISTS  administrador;
DROP ROLE IF EXISTS  comite;
DROP ROLE IF EXISTS  estudiante;

DROP VIEW IF EXISTS vw_comite_vista;
DROP VIEW IF EXISTS vw_estudiante_solicitudes;


-- VISTAS
-- COMITE
CREATE VIEW vw_comite_vista AS
SELECT solId, perCedulaEstudiante, solTipo, solEstado FROM estudiante_has_solicitud natural join solicitud;

-- ESTUDIANTE
CREATE VIEW vw_estudiante_solicitudes AS
SELECT *
FROM solicitud NATURAL JOIN estudiante_has_solicitud;

-- ROL DE EDITOR
CREATE ROLE administrador;
GRANT ALL ON solicitudes_consejo.* TO administrador;

-- ROL DE ESTUDIANTE
CREATE ROLE estudiante;
GRANT SELECT, INSERT ON solicitudes_consejo.vw_estudiante_solicitudes TO estudiante;
GRANT SELECT ON solicitudes_consejo.nombresSolicitudes TO estudiante;
GRANT SELECT ON solicitudes_consejo.requisitosNombres TO estudiante;
GRANT SELECT ON solicitudes_consejo.solicitudes_has_requisitos TO estudiante;
GRANT EXECUTE ON PROCEDURE solicitudes_consejo.estudiante_ver_solicitud TO estudiante;
GRANT EXECUTE ON PROCEDURE solicitudes_consejo.estudiante_crear_solicitud TO estudiante;
GRANT EXECUTE ON PROCEDURE solicitudes_consejo.cedula_estudiante TO estudiante;
GRANT EXECUTE ON PROCEDURE solicitudes_consejo.solicitudes_nombres TO estudiante;
GRANT EXECUTE ON PROCEDURE solicitudes_consejo.solicitudes_requisitos TO estudiante;

-- ROL DE COMITE
CREATE ROLE comite;
GRANT SELECT ON solicitudes_consejo.vw_comite_vista TO comite;
GRANT EXECUTE ON PROCEDURE solicitudes_consejo.vista_del_comite TO comite;
GRANT EXECUTE ON PROCEDURE solicitudes_consejo.update_estado TO comite;
GRANT EXECUTE ON PROCEDURE solicitudes_consejo.carrera_pasar_facultad TO comite;
GRANT EXECUTE ON PROCEDURE solicitudes_consejo.sede_pasar_csu TO comite;
GRANT EXECUTE ON PROCEDURE solicitudes_consejo.miembros_del_comite TO comite;

-- CREACION DE USUARIOS
CREATE USER 'estudianteX'@'localhost' IDENTIFIED BY '12345678';
CREATE USER 'comite_sede'@'localhost' IDENTIFIED BY '87654321';
CREATE USER 'admin1'@'localhost' IDENTIFIED BY 'A12345678';

-- ASIGNACION DE ROLES A LOS USUARIOS
GRANT estudiante TO 'estudianteX'@'localhost';
SET DEFAULT ROLE estudiante TO 'estudianteX'@'localhost'; 

GRANT comite TO 'comite_sede'@'localhost';
SET DEFAULT ROLE comite TO 'comite_sede'@'localhost'; 

GRANT administrador TO 'admin1'@'localhost';
SET DEFAULT ROLE administrador TO 'admin1'@'localhost';


drop table if exists loginadmin;
create table loginadmin (userr int auto_increment key not null, usuario varchar(100), contrasena varchar(100));
insert into loginadmin values (1, 'admin1', 'A12345678');

drop table if exists logincomite;
create table logincomite (userr int auto_increment key not null, usuario varchar(100), contrasena varchar(100));
UPDATE logincomite SET contrasena = 'S87654321' WHERE userr = 1;
insert into logincomite values (1, 'comite_sede', 'S87654321');
insert into logincomite values (2, 'comite_facultad', 'F87654321');
insert into logincomite values (3, 'comite_csu', 'C87654321');

drop table if exists loginestudiantes;
create table loginestudiantes (usuario varchar(100) key, contrasena varchar(100));
insert into loginestudiantes values ('fvalderramab', '12345678');
insert into loginestudiantes values ('dieramirezma', '12345678');
insert into loginestudiantes values ('axgomezm', '12345678');
insert into loginestudiantes values ('bforerob', '12345678');
insert into loginestudiantes values ('glondonot', '12345678');
insert into loginestudiantes values ('antoniop', '12345678');
insert into loginestudiantes values ('josep', '12345678');
insert into loginestudiantes values ('manuelp', '12345678');
insert into loginestudiantes values ('franciscop', '12345678');
insert into loginestudiantes values ('davidp', '12345678');
insert into loginestudiantes values ('juanp', '12345678');
insert into loginestudiantes values ('josuep', '12345678');
insert into loginestudiantes values ('javierp', '12345678');
insert into loginestudiantes values ('danielp', '12345678');
insert into loginestudiantes values ('luisp', '12345678');
insert into loginestudiantes values ('isabellap', '12345678');
insert into loginestudiantes values ('oliviap', '12345678');
insert into loginestudiantes values ('alexisp', '12345678');
insert into loginestudiantes values ('sofiap', '12345678');
insert into loginestudiantes values ('victoriap', '12345678');
insert into loginestudiantes values ('ameliap', '12345678');
insert into loginestudiantes values ('alexap', '12345678');
insert into loginestudiantes values ('juliap', '12345678');
insert into loginestudiantes values ('julianp', '12345678');
insert into loginestudiantes values ('julianap', '12345678');
insert into loginestudiantes values ('camilap', '12345678');
insert into loginestudiantes values ('alexandrap', '12345678');
insert into loginestudiantes values ('garciap', '12345678');
insert into loginestudiantes values ('gonzalezp', '12345678');
insert into loginestudiantes values ('rodriguezp', '12345678');
insert into loginestudiantes values ('fernandezp', '12345678');
insert into loginestudiantes values ('lopezp', '12345678');

select*from vw_comite_vista;
select*from vw_estudiante_solicitudes;
select*from estudiante_has_solicitud;