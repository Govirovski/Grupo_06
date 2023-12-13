drop database grupo06;

create database grupo06;

use grupo06;

create table usuarios (
    id int auto_increment primary key,
    correo varchar(255) unique not null,
    contraseña varchar(255) not null
);

insert usuarios (correo, contraseña) values ('Eduardo@gmail.com', 'Lalo12025');

select * from usuarios;

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

