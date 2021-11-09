DROP USER IF EXISTS 'news_user'@'localhost';
--
DROP DATABASE IF EXISTS news_db;
--
FLUSH PRIVILEGES;
--
CREATE USER 'news_user'@'localhost'
IDENTIFIED BY 'news_pass';
--
CREATE DATABASE news_db;
--
GRANT ALL PRIVILEGES ON news_db.*
TO 'news_user'@'localhost';
--
USE news_db;
--
CREATE TABLE news (
id INT(11) NOT NULL AUTO_INCREMENT,
text TEXT,
dapa TEXT,
tema_id INT(11),
PRIMARY KEY (id)
);
--
CREATE TABLE tema (
id INT(11) NOT NULL AUTO_INCREMENT,
name TEXT,
PRIMARY KEY (id)
);
--
ALTER TABLE news
ADD FOREIGN KEY (tema_id)
REFERENCES tema(id)
ON DELETE CASCADE
ON UPDATE CASCADE;
--
INSERT INTO tema VALUES ("0","Экзамены, ВПР");
INSERT INTO tema VALUES ("0","Праздники");
INSERT INTO tema VALUES ("0","Действительно важно");
--
INSERT INTO news VALUES ("0","Проводится ОГЭ по математике в Лицее № 15.","2021.06.31","1");
INSERT INTO news VALUES ("0","Проводится ВПР по истории у 7 классов в МБОУ СОШ №12 в к.12.","2021.04.02","1");
INSERT INTO news VALUES ("0","Проводится ЕГЭ по информатике в Лицее №15","2021.06.24","1");
INSERT INTO news VALUES ("0","Поздравляем Гаврюшину Любовь Сергеевну с 60-летием!","2021.08.07","2");
INSERT INTO news VALUES ("0","Поздравляем всех с днем учителя!","2021.10.05","2");
INSERT INTO news VALUES ("0","Поздравляем с днем Алкоголика!!!!","2021.02.20","2");
INSERT INTO news VALUES ("0","Ждем всех на субботник в 12 часов дня у школы №12.","2021.10.30","3");
INSERT INTO news VALUES ("0","Конец света!!","2022.01.01","3");
INSERT INTO news VALUES ("0","У нас новый директор!!","2021.11.09","3");
--
