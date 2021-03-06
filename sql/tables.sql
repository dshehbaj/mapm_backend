drop database if exists mapm;
create database mapm;
use mapm;

create table States (
  code varchar(5) primary key,
  name varchar(50) not null
);

create table Counties (
  id varchar(50) primary key,
  name varchar(50) not null,
  state varchar(5) not null,
  lat double,
  lng double,
  constraint FK_state_code foreign key (state) references States(code)
    on delete cascade
);

create table State_life_expec (
  state varchar(5) not null,
  age double not null,
  constraint FK_state_code_expec foreign key (state) references States(code)
    on delete cascade
);

create table County_life_expec (
  cnty varchar(50) not null,
  age double not null
);

create table State_real_estate (
  state varchar(5) not null,
  price double not null,
  constraint FK_state_code_estate foreign key (state) references States(code)
    on delete cascade
);

create table County_real_estate (
  cnty varchar(50) not null,
  price double not null
);

create table State_vaccinations (
  state varchar(5) not null,
  total_vaccinations int not null,
  total_distributed int not null,
  people_vaccinated int not null,
  people_fully_vaccinated_per_hundred double not null,
  total_vaccinations_per_hundred double not null,
  people_fully_vaccinated int not null,
  people_vaccinated_per_hundred double not null,
  distributed_per_hundred double not null,
  daily_vaccinations_raw int not null,
  daily_vaccinations int not null,
  daily_vaccinations_per_million double not null,
  share_doses_used double not null,
  constraint FK_state_code_vacc foreign key (state) references States(code)
    on delete cascade
);

