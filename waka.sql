drop database IF EXISTS WakaDB;
create database WakaDB CHARACTER SET utf8 COLLATE utf8_general_ci;
use WakaDB;

create table Customer (
    customerNo INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name char(32),
    phone char(32),
    address char(255),
    gender char(6),
    birthday date,

    UNIQUE KEY (name, phone)
) DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

create table Membership (
    membershipNo INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    regDate date,
    balance decimal(19,4),
    passphrase char(32),

    customerNo integer not null,
    foreign key(customerNo) references Customer(customerNo) on update cascade
) DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

create table Product (
    productNo INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name char(32),
    count integer,
    price decimal(19,4),
    details char(255)
) DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

create table Purchasing (
    purNo INT NOT NULL AUTO_INCREMENT PRIMARY KEY,

    productNo integer not null,
    foreign key(productNo) references Product(productNo) on update cascade,

    count integer,
    payment decimal(19,4),
    dtime datetime,

    membershipNo integer not null,
    foreign key(membershipNo) references Membership(membershipNo) on update cascade
) DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

create table Expenditure (
    expNo INT NOT NULL AUTO_INCREMENT PRIMARY KEY,

    dtime datetime,
    payment decimal(19,4),
    details char(255),

    productNo integer,
    foreign key(productNo) references Product(productNo) on update cascade
) DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/*Test data*/
insert into Customer values(null, "张健明", "13730644652", "东公元", "男", "1982-09-13");
insert into Customer values(null, "陈超", "13730644651", "万科海悦汇城", "男", "1983-10-01");
insert into Membership values(null, "2016-01-01", 100.00, "吃俺老孙一棒", (select customerNo from Customer where phone="13730644651"));
insert into Product values(null, "Prod1", 30, 7.50, "Prod1 Descriptions.");
insert into Product values(null, "Prod2", 20, 25.0, "Prod2 Descriptions."); 
insert into Purchasing values(null, (select productNo from Product where name="Prod1"), 2, 15.00, "2016-01-02", (select membershipNo from Membership where passphrase="吃俺老孙一棒"));

insert into Expenditure values(null, "2016-01-01", 1000.00, "房租", null);


