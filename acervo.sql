create database acervo;
use acervo;

create table livros(
codigo int primary key auto_increment,
titulo varchar(100) not null,
autor varchar(100),
editora varchar(100));

