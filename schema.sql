-- init database

drop database if exists test;

create database test;

use test;

grant select, insert, update, delete on test.* to 'www-data'@'localhost' identified by 'www-data';

create table contact (
    `id` varchar(50) not null,
    `name` varchar(50) not null,
    `tel` varchar(50) not null,
    `work_tel` varchar(50) not null,
    `sex` varchar(50) not null,
    `college` varchar(50) not null,
    `headman` bool not null,
    `groupid` varchar(50) not null,
    `year` varchar(50) not null,
    primary key (`id`)
) engine=innodb default charset=utf8;
-- email / password:
-- admin@example.com / password

