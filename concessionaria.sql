create database concessionaria;

use concessionaria;

create table veiculos(
codigo int primary key auto_increment,
modelo varchar(100),
ano int,
valor float);

INSERT INTO veiculos (modelo, ano, valor) VALUES ('Fiat Uno', 2010, 18000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Chevrolet Onix', 2018, 52000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Volkswagen Gol', 2012, 25000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Ford Ka', 2016, 32000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Hyundai HB20', 2020, 65000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Renault Sandero', 2015, 28000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Toyota Corolla', 2021, 95000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Honda Civic', 2019, 85000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Jeep Compass', 2022, 135000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Nissan Kicks', 2020, 87000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Fiat Mobi', 2021, 46000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Peugeot 208', 2022, 73000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Citroën C3', 2013, 27000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Chevrolet Prisma', 2017, 40000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Ford EcoSport', 2014, 38000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Volkswagen Voyage', 2012, 26000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Hyundai Creta', 2021, 112000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Renault Kwid', 2023, 48000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Toyota Hilux', 2022, 210000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Honda Fit', 2018, 62000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Fiat Toro', 2021, 128000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Chevrolet S10', 2020, 155000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Volkswagen T-Cross', 2023, 122000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Ford Ranger', 2019, 149000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Jeep Renegade', 2022, 108000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Nissan Frontier', 2018, 138000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Hyundai Tucson', 2016, 67000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Renault Logan', 2014, 30000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Toyota Etios', 2015, 29000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Honda HR-V', 2020, 109000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Fiat Siena', 2011, 23000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Chevrolet Spin', 2017, 43000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Volkswagen Fox', 2013, 27000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Ford Fiesta', 2014, 31000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Jeep Wrangler', 2023, 250000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Nissan Versa', 2021, 68000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Hyundai Elantra', 2019, 77000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Renault Duster', 2020, 74000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Toyota Yaris', 2021, 67000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Honda City', 2022, 89000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Fiat Palio', 2009, 18000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Chevrolet Tracker', 2023, 119000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Volkswagen Polo', 2022, 87000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Ford Maverick', 2023, 170000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Jeep Grand Cherokee', 2025, 275000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Nissan Sentra', 2018, 67000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Hyundai i30', 2015, 52000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Renault Captur', 2021, 91000.00);
INSERT INTO veiculos (modelo, ano, valor) VALUES ('Toyota SW4', 2025, 310000.00);

# 1. listar todos os dados
select * from veiculos;

# 1.5  exibir apenas algumas colunas
select modelo, ano from veiculos;

# 2. listar ordenando pelo valor
select * from veiculos ORDER BY valor;

# 2.5 ordenar por mais de uma coluna
select * from veiculos order by ano, valor;

# order by estado, cidade, bairro;

# 3. listar em ordem decrescente pelo ano
select * from veiculos order by ano DESC;

# 3.5 crescente e decrescente no mesmo comando
select * from veiculos order by ano DESC, valor ASC;

# 4. listar veículos fabricados entre 2010 e 2020 (inclusive) usando AND
select * from veiculos
WHERE ano >= 2010 AND ano <= 2020
order by ano;

# 4.5 veiculos do ano 2014 que custam menos de 35000
select * from veiculos
where ano = 2014 and valor < 35000;

# 5. repita o anterior usando BETWEEN
select * from veiculos
where ano between 2010 and 2020
order by ano;

# pesquisa textual ##################################
# 6. listar veículos fabricados pela FIAT
select * from veiculos
where modelo LIKE "Fiat%";  #  % - qualquer texto depois de Fiat

select * from veiculos 
where modelo LIKE "%Gol";  # termina com Gol

select * from veiculos
where modelo like "%to%";  # a silaba/palavra aparece em qualquer parte

# 7. listar informações sobre Palio ou Fiesta
select * from veiculos
where modelo like "%Palio%" 
OR modelo like "%Fiesta%";

# 8. listar veículos fabricados pela TOYOTA ou FORD
select modelo from veiculos
where modelo like "%Toyota%" 
OR modelo like "%Ford%" order by modelo;

# Pesquisa usando IN (conjunto) ####
# 9. listar veículos dos anos 2015, 2018, 2021
select * from veiculos
where ano IN (2015, 2018, 2021) order by ano;

# where estado in ("RN", "CE", "BA", "SP");

select * from veiculos
where ano = 2015 or ano = 2018 or ano = 2021;

# 10. listar veiculos da honda com valor menor ou igual a 85000
select * from veiculos
where modelo like "%honda%" and valor <= 85000;

# FUNÇÕES AGREGADAS
# 11. somar o valor de todos os veiculos da concessionária SUM

# 12. média de valor dos veiculos da concessionária AVG

# 13. média de valor dos veículos chevrolet

# 14. contar quantos veículos há na concessionária COUNT

# 15. contar os veículos da nissan estão cadastrados

# 16. valor do veículo mais caro MAX

# 17. valor do veículo mais barato MIN

## SUB-CONSULTAS ######################################

# 18. todas as informações do veículo mais caro 

# 19. todas as informações do veículo mais barato

# 20. veículos cujo preço é abaixo da média de preços