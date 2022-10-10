create database imobiliaria;

create table proprietario(
    id_proprietario integer primary key,
    nome_proprietario varchar(200) not null);
	
create table imovel(
    id_imovel integer primary key);
	
create table endereco(
    id_endereco integer primary key,
    rua varchar(200) not null,
    bairro varchar(200) not null,
    numero varchar(5) not null,
    id_imovel integer not null,
    constraint fk_id_imovel_endereco
    foreign key (id_imovel)
    references imovel(id_imovel)
    );

create table inquilino(
    id_inquilino integer primary key,
    nome_inquilino varchar(200) not null);
	
create table corretor(
    id_corretor integer primary key,
    nome_corretor varchar(200) not null);

create table telefone_inquilino(
    id_telefone_inquilino integer primary key,
    numero_telefone varchar(16) not null,
    id_inquilino integer not null,
    constraint fk_id_telefone_inquilino
    foreign key (id_inquilino)
    references inquilino(id_inquilino)
    );