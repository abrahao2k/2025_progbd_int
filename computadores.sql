create database computadores;
use computadores;

create table pc(
codigo int primary key auto_increment,
marca varchar(100),
processador varchar(100),
memoria int,
armazenamento int);