@echo off
%apache% --start
%mda2sql% init.mda
%mysql% --start

mysql -u root -p
  source init.sql;
  show databases;
  use news_db;
  show tables;
  select text from news;


%apache% --stop
%mysql% --stop
