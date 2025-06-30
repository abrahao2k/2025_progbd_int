#CRIAR BANCO DE DADOS
create database escola;
create database biblioteca;

#USAR UM BANCO DE DADOS
use escola;
use biblioteca;

# CRIAR UMA TABELA
create table aluno(
codigo int primary key auto_increment,
nome varchar(100),
curso varchar(100) );

# INSERIR DADOS NA TABELA
insert into aluno values(1, 'Ana', 'Informática');
insert into aluno values(null, 'Rodrigo', 'Informática');
insert into aluno values(null, 'Fátima', 'Edificações');
insert into aluno values(9, 'Maria', 'Edificações');
insert into aluno values(null, 'Pedro', 'Mecânica');


# INDICAR A/S COLUNAS QUE QUER PREENCHER
insert into aluno (nome) values ('Carlos');
insert into aluno (curso) values ('Eletrotécnica');
insert into aluno (codigo, nome) values (13,'Katia');

# EXIBIR OS DADOS DA TABELA
select * from aluno;


create database biblioteca; # se não criou ainda
use biblioteca;
create table livro(codigo int, titulo varchar(100));

# EXCLUIR UMA TABELA - não tem volta, cuidado!
drop table livro;

# EXCLUIR UM BANCO - não tem volta, cuidado!
drop database biblioteca;

# EXIBIR OS BANCOS DE UM SERVIDOR
show databases;

# EXIBIR AS TABELAS DE UM BANCO
use mysql; # escolha o banco
show tables;









