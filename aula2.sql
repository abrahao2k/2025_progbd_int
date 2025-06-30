create database restaurante;
use restaurante;
create table pratos(
codigo int primary key auto_increment,
descricao varchar(100) not null,
preco float);

insert into pratos values (null, "Cuscuz", 5.00);
insert into pratos values (null, "Arroz", 7.50);
insert into pratos values (null, "Feijão", 12.00);

select * from pratos; #exibe os dados da tabela

# ORDENAR OS RESULTADOS DE UMA CONSULTA SELECT
select * from pratos ORDER BY descricao;

# ORDEM DECRESCENTE (do maior para o menor)
select * from pratos ORDER BY preco DESC;

insert into pratos values(null, "Parmegiana", 25.00);
insert into pratos values(null, "Espaguete", 18.00);
insert into pratos values(null, "Bife", 13.50);
insert into pratos values(null, "Limonada", 8.25);

# EXIBIR APENAS AS COLUNAS INDICADAS
select descricao, preco from pratos;

select descricao, preco 
from pratos 
order by descricao;      # pode ordenar

# FILTRAR USANDO UMA CONDIÇÃO
# pratos que custam menos de 10 Reais
select * from pratos WHERE preco < 10;

# pratos que custam mais de 15 reais
select * from pratos WHERE preco > 15;

# igual  =
# diferente  <>  ou  !=
# maior ou igual >=
# menor ou igual <=

insert into pratos values(null,"Arroz", 10.00);

# SELEÇÃO PELO CÓDIGO / CHAVE PRIMÁRIA
# garante que apenas 1 item será exibido
select * from pratos where descricao = "Arroz";

select * from pratos where codigo = 2;

# ATUALIZAR OS DADOS DE UM REGISTRO EXISTENTE
# atualizar o preço do arroz (codigo 2) para 5.00
update pratos       # atualize a tabela pratos
set preco = 8.00    # defina o preço como 5.00
where codigo = 2;   # onde o código é 2

# atualizar mais de uma coluna ao mesmo tempo
update pratos
set descricao = "Arroz de Leite", preco = 15
where codigo = 8;

# atualizar vários itens ao mesmo tempo 
# a condição precisa atender os vários itens
update pratos
set preco = 0
where codigo > 5;   # CUIDADO, não dá pra desfazer!

# EXCLUIR UM REGISTRO
delete from pratos
where codigo = 6;   # CUIDADO, não dá pra desfazer!

select * from pratos;





