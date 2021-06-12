create database beex;
use beex;
create table bx_profile (     ID int not null ,
     slug varchar(35) not null ,
     display_name varchar(65) not null ,
     settings     json null 
	comment 'preferences { 	module:{view ,edit ,delete (...)} }' ,
     estatus      varchar(3) default 'a' null 
	comment 'sub entity: estatus ' ,
     constraint bx_profile_pk primary key (ID) ) 
	comment 'beex:profile' ;
  create unique index bx_profile_slug_uindex 	on bx_profile (slug) ;
  create table bx_user (     ID       bigint auto_increment ,
     hash_key varchar(255) not null ,
     username varchar(65)  not null ,
     fullname varchar(150) null ,
     email    varchar(200) not null ,
     age      int        default 18 null ,
     gender   char       default 'm' null 
	comment 'sub entity: gender m: male f: female o: other' ,
     estatus  varchar(3) default 'a' null 
	comment 'sub entity: estatus a: active u: unactive p: pending b: banned d: deleted' ,
     metadata json null 
	comment 'other data { 	photo: 	wallpaper: 	(...) }' ,
     constraint bx_user_pk primary key (ID) ) 
	comment 'beex:user' ;
  create unique index bx_user_hash_key_uindex 	on bx_user (hash_key) ;
  alter table bx_user 	add phone varchar(35) null 
	comment 'regex (phone format)' after email ;

alter table bx_user
	add identification varchar(55) null after phone;

create unique index bx_user_identification_uindex
	on bx_user (identification);
