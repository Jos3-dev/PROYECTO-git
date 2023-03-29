CREATE DATABASE IF NOT EXISTS pruebaDeDelete;
SHOW DATABASES;
USE holamundo;
drop table pruebadedelete;

CREATE TABLE IF NOT EXISTS user (
	id int not null auto_increment,
    nombre varchar(50) not null,
    edad int not null,
    email varchar(100) not null,
    primary key(id)
);

INSERT	INTO user (nombre, edad, email) VALUES ('oscar', 25, 'oscar@gmail.com');
INSERT	INTO user (nombre, edad, email) VALUES ('laya', 15, 'laya@gmail.com');
INSERT	INTO user (nombre, edad, email) VALUES ( 'nicolas', 36, 'nicolas@gmail.com');
INSERT INTO	user (nombre, edad, email) VALUES ( 'chanchito', 7, 'chanchito@gmail.com');

SELECT * FROM user;
SELECT * FROM user LIMIT 3;
SELECT * FROM user WHERE edad > 15;
SELECT * FROM user WHERE edad >= 15;
SELECT * FROM user where edad > 20 and email = 'nicolas@gmail.com';
SELECT * FROM user WHERE edad > 20 or email = 'laya@gmail.com';
SELECT * FROM user WHERE email != 'laya@gmail.com';
SELECT * FROM user WHERE edad between 15 and 30;

-- busca los elementos que tenga los caracteres dentro de la cadena (no importa lo suceso y lo subsecuente)
SELECT * FROM user WHERE email like '%gmail%';
-- busca elementos que terminen en gmail
SELECT * FROM user WHERE email like '%gmail';
SELECT * FROM user WHERE email like 'oscar%';

-- ordenar columna edad de forma ascendente y descendiente
select * FROM user order by edad asc;
select * FROM user order by edad desc;

-- buscar por mayor edad en columna edad
SELECT MAX(edad) as mas_viejo from user;
SELECT MIN(edad) as Mas_joven FROM user;

-- filtrar por columnas solamente
SELECT id, nombre FROM user;
SELECT id as IDENTIFICADOR, nombre as NAME_perro FROM user;


-- TUTORIAL DE HOLA MUNDO
# TE QUEDASTE EN EL MINUTO 1:14:30