drop database grupo06;
drop table respuestas;
create database grupo06;

use grupo06;

create table usuarios (
    id int auto_increment primary key,
    correo varchar(255) unique not null,
    contraseña varchar(255) not null
);

INSERT INTO usuarios (correo, contraseña)
VALUES
	('Eduardo@gmail.com', 'Lalo12025'),
	('Omar@gmail.com', 'omar11'),
	('pedro@gmail.com', 'pedro01'),
	('alberto@gmail.com', 'rojas100'),
	('francis@gmail.com', 'francis02'),
	('sapo@gmail.com', 'sapo111'),
	('patito@gmail.com', 'minipato'),
	('itadori@gmail.com', 'muere15'),
	('satoru@gmail.com', 'azul1010'),
	('gojo@gmail.com', 'xdxd'),
	('sukuna@gmail.com', 'good1'),
	('jjt@gmail.com', 'sapoeres');

select * from usuarios;
	select * from respuestas;

create table respuestas (
    id int auto_increment primary key,
    palabra_clave varchar(255)  not null,
    respuesta text not null
);

INSERT INTO respuestas (palabra_clave, respuesta) VALUES
    ('hola,hi,saludos,buenas', 'Hola soy Tu Botsito preferido'),
    ('como,estas,va,vas,sientes', 'Estoy bien y tu?'),
    ('gracias,te lo agradezco,thanks', 'Siempre a la orden'),
	('semanas, lineamiento, entrega, evidencia, curso, cuales', 'Lineamientos AA1 - AA4 \n AA1 - https://campusdigital.certus.edu.pe/mod/resource/view.php?id=640461\n AA2 - https://campusdigital.certus.edu.pe/mod/resource/view.php?id=640462\n AA3 - https://campusdigital.certus.edu.pe/mod/resource/view.php?id=640463\n AA4 - https://campusdigital.certus.edu.pe/mod/resource/view.php?id=640464'),
	('rubrica, evidencia AA1', 'Rúbrica AA1 - https://campusdigital.certus.edu.pe/mod/resource/view.php?id=640465'),
	('criterios de evaluacion, criterios', 'criterios de evaluación - https://campusdigital.certus.edu.pe/pluginfile.php/746235/mod_resource/content/0/R%C3%BAbrica%20AA2.pdf'),
	('individual, grupal, la evaluación de la evidencia es grupal o individual', 'lineamiento solicitado - \n https://campusdigital.certus.edu.pe/pluginfile.php/746231/mod_resource/content/0/Lineamientos%20de%20evaluaci%C3%B3n%20AA2.pdf'),
	('lineamientos, ver lineamientos, mis lineamientos, calificacion', 'Ver lineamientos'),
	('notas, ver notas, mis notas, notas del curso, donde puedo visualizar mis notas', 'Ver tus notas'),
	('cuando puedo ver notas, semanas de visualización, En que semanas puedo visualizar las notas del curso?', 'Una semana después de la presentación de cada una de tus evidencias.');

INSERT INTO respuestas (palabra_clave, respuesta) VALUES ('desconocida', 'no entendí tu consulta; No estoy seguro de lo que quieres; Disculpa, ¿puedes intentarlo de nuevo?');

INSERT INTO respuestas (palabra_clave, respuesta) VALUES
    ('modalidad,modalidad del curso,Cual es la modalidad del curso?', 'La modalidad del curso es 100% virtual'),
    ('competencia,competencias,competencias del curso,Cuales son las competencias del curso?', 'Competencias del curso - https://campusdigital.certus.edu.pe/pluginfile.php/746228/mod_resource/content/0/DDS_Sílabo_Diseño%20de%20Soluciones%20con%20Inteligencia%20Artificial_VI%20ciclo.pdf'),
    ('evaluacion,evaluaciones,evaluaciones calificadas,Cuantas evaluaciones calificadas tiene el curso?', 'Evaluaciones calificadas del curso - https://campusdigital.certus.edu.pe/pluginfile.php/746228/mod_resource/content/0/DDS_Sílabo_Diseño%20de%20Soluciones%20con%20Inteligencia%20Artificial_VI%20ciclo.pdf');


