CREATE USER 'lala_user'@'localhost'
IDENTIFIED BY 'lala_pass';
--
CREATE DATABASE lala_db;
--
GRANT ALL PRIVILEGES ON lala_db.*
TO 'lala_user'@'localhost';
--
USE lala_db;
--
CREATE TABLE day (
id INT(11) NOT NULL AUTO_INCREMENT,
name TEXT,
PRIMARY KEY (id)
);
--
CREATE TABLE cabinet (
id INT(11) NOT NULL AUTO_INCREMENT,
name TEXT,
short_name TEXT,
PRIMARY KEY (id)
);
--
CREATE TABLE subject (
id INT(11) NOT NULL AUTO_INCREMENT,
name TEXT,
short_name TEXT,
PRIMARY KEY (id)
);
--
CREATE TABLE weekday (
id INT(11) NOT NULL AUTO_INCREMENT,
name TEXT,
short_name TEXT,
n INT(11),
PRIMARY KEY (id)
);
--
CREATE TABLE lapse (
id INT(11) NOT NULL AUTO_INCREMENT,
n INT(11),
start_time TEXT,
end_time TEXT,
PRIMARY KEY (id)
);
--
CREATE TABLE teacher (
id INT(11) NOT NULL AUTO_INCREMENT,
surname TEXT,
name TEXT,
patronymic TEXT,
short_name TEXT,
PRIMARY KEY (id)
);
--
CREATE TABLE class (
id INT(11) NOT NULL AUTO_INCREMENT,
name TEXT,
short_name TEXT,
PRIMARY KEY (id)
);
--
CREATE TABLE lesson (
id INT(11) NOT NULL AUTO_INCREMENT,
day_id INT(11),
weekday_id INT(11),
lapse_id INT(11),
subject_id INT(11),
cabinet_id INT(11),
teacher_id INT(11),
class_id INT(11),
PRIMARY KEY (id)
);
--
ALTER TABLE lesson
ADD FOREIGN KEY (day_id)
REFERENCES day(id)
ON DELETE CASCADE
ON UPDATE CASCADE;
--
ALTER TABLE lesson
ADD FOREIGN KEY (weekday_id)
REFERENCES weekday(id)
ON DELETE CASCADE
ON UPDATE CASCADE;
--
ALTER TABLE lesson
ADD FOREIGN KEY (lapse_id)
REFERENCES lapse(id)
ON DELETE CASCADE
ON UPDATE CASCADE;
--
ALTER TABLE lesson
ADD FOREIGN KEY (subject_id)
REFERENCES subject(id)
ON DELETE CASCADE
ON UPDATE CASCADE;
--
ALTER TABLE lesson
ADD FOREIGN KEY (cabinet_id)
REFERENCES cabinet(id)
ON DELETE CASCADE
ON UPDATE CASCADE;
--
ALTER TABLE lesson
ADD FOREIGN KEY (teacher_id)
REFERENCES teacher(id)
ON DELETE CASCADE
ON UPDATE CASCADE;
--
ALTER TABLE lesson
ADD FOREIGN KEY (class_id)
REFERENCES class(id)
ON DELETE CASCADE
ON UPDATE CASCADE;
--
INSERT INTO day VALUES ("0","2021.10.11");
INSERT INTO day VALUES ("0","2021.10.12");
INSERT INTO day VALUES ("0","2021.10.13");
INSERT INTO day VALUES ("0","2021.10.14");
INSERT INTO day VALUES ("0","2021.10.15");
--
INSERT INTO cabinet VALUES ("0","Актовый зал","акт.");
INSERT INTO cabinet VALUES ("0","Учительская","уч.");
INSERT INTO cabinet VALUES ("0","Улица","ул.");
INSERT INTO cabinet VALUES ("0","Столярная мастерская","мас.");
INSERT INTO cabinet VALUES ("0","Спортивный зал","с/з");
INSERT INTO cabinet VALUES ("0","Кабинет № 1","к.1");
INSERT INTO cabinet VALUES ("0","Кабинет № 2","к.2");
INSERT INTO cabinet VALUES ("0","Кабинет № 3","к.3");
INSERT INTO cabinet VALUES ("0","Кабинет № 4","к.4");
INSERT INTO cabinet VALUES ("0","Кабинет № 5","к.5");
INSERT INTO cabinet VALUES ("0","Кабинет № 6","к.6");
INSERT INTO cabinet VALUES ("0","Кабинет № 7","к.7");
INSERT INTO cabinet VALUES ("0","Кабинет № 8","к.8");
INSERT INTO cabinet VALUES ("0","Кабинет № 9","к.9");
INSERT INTO cabinet VALUES ("0","Кабинет № 10","к.10");
INSERT INTO cabinet VALUES ("0","Кабинет № 11","к.11");
INSERT INTO cabinet VALUES ("0","Кабинет № 12","к.12");
INSERT INTO cabinet VALUES ("0","Кабинет № 13","к.13");
INSERT INTO cabinet VALUES ("0","Кабинет № 14","к.14");
INSERT INTO cabinet VALUES ("0","Кабинет № 15","к.15");
INSERT INTO cabinet VALUES ("0","Кабинет № 16","к.16");
INSERT INTO cabinet VALUES ("0","Кабинет № 17","к.17");
INSERT INTO cabinet VALUES ("0","Кабинет № 18","к.18");
INSERT INTO cabinet VALUES ("0","Кабинет № 19","к.19");
INSERT INTO cabinet VALUES ("0","Кабинет № 20","к.20");
INSERT INTO cabinet VALUES ("0","Кабинет № 21","к.21");
INSERT INTO cabinet VALUES ("0","Кабинет № 22","к.22");
INSERT INTO cabinet VALUES ("0","Кабинет № 23","к.23");
INSERT INTO cabinet VALUES ("0","Кабинет № 24","к.24");
INSERT INTO cabinet VALUES ("0","Кабинет № 25","к.25");
INSERT INTO cabinet VALUES ("0","Кабинет № 26","к.26");
INSERT INTO cabinet VALUES ("0","Кабинет № 27","к.27");
--
INSERT INTO weekday VALUES ("0","Воскресенье","вс","0");
INSERT INTO weekday VALUES ("0","Понедельник","пн","1");
INSERT INTO weekday VALUES ("0","Вторник","вт","2");
INSERT INTO weekday VALUES ("0","Среда","ср","3");
INSERT INTO weekday VALUES ("0","Четверг","чт","4");
INSERT INTO weekday VALUES ("0","Пятница","пт","5");
INSERT INTO weekday VALUES ("0","Суббота","cб","6");
--
INSERT INTO subject VALUES ("0","Физкультура","Физ-ра");
INSERT INTO subject VALUES ("0","Литература","Литература");
INSERT INTO subject VALUES ("0","Технология","Технология");
INSERT INTO subject VALUES ("0","Русский язык","Рус.яз.");
INSERT INTO subject VALUES ("0","Математика","Математика");
INSERT INTO subject VALUES ("0","ИЗО","ИЗО");
INSERT INTO subject VALUES ("0","Музыка","Музыка");
INSERT INTO subject VALUES ("0","Немецкий язык","Нем.яз.");
INSERT INTO subject VALUES ("0","Английский язык","Англ.яз.");
INSERT INTO subject VALUES ("0","Биология","Биология");
INSERT INTO subject VALUES ("0","Химия","Химия");
INSERT INTO subject VALUES ("0","Физика","Физика");
INSERT INTO subject VALUES ("0","География","География");
INSERT INTO subject VALUES ("0","ОБЖ","ОБЖ");
INSERT INTO subject VALUES ("0","История","История");
INSERT INTO subject VALUES ("0","Астрономия","Астрономия");
INSERT INTO subject VALUES ("0","Обществознание","Общество");
INSERT INTO subject VALUES ("0","Экономика","Экономика");
INSERT INTO subject VALUES ("0","Право","Право");
INSERT INTO subject VALUES ("0","-","-");
INSERT INTO subject VALUES ("0","Классный час","Кл.ч");
--
INSERT INTO lapse VALUES ("0","0","08:30","09:15");
INSERT INTO lapse VALUES ("0","1","09:30","10:20");
INSERT INTO lapse VALUES ("0","2","10:30","11:20");
INSERT INTO lapse VALUES ("0","3","11:30","12:20");
--
INSERT INTO class VALUES ("0","1 A","1 A");
INSERT INTO class VALUES ("0","1 Б","1 Б");
INSERT INTO class VALUES ("0","1 В","1 В");
INSERT INTO class VALUES ("0","2 А","2 А");
INSERT INTO class VALUES ("0","2 Б","2 Б");
INSERT INTO class VALUES ("0","2 В","2 В");
INSERT INTO class VALUES ("0","3 А","3 А");
INSERT INTO class VALUES ("0","3 Б","3 Б");
INSERT INTO class VALUES ("0","3 В","3 В");
INSERT INTO class VALUES ("0","4 А","4 А");
INSERT INTO class VALUES ("0","4 Б","4 Б");
INSERT INTO class VALUES ("0","4 В","4 В");
INSERT INTO class VALUES ("0","5 А","5 А");
INSERT INTO class VALUES ("0","5 Б","5 Б");
INSERT INTO class VALUES ("0","5 В","5 В");
INSERT INTO class VALUES ("0","6 А","6 А");
INSERT INTO class VALUES ("0","6 Б","6 Б");
INSERT INTO class VALUES ("0","6 В","6 В");
INSERT INTO class VALUES ("0","7 А","7 А");
INSERT INTO class VALUES ("0","7 Б","7 Б");
INSERT INTO class VALUES ("0","7 В","7 В");
INSERT INTO class VALUES ("0","8 А","8 А");
INSERT INTO class VALUES ("0","8 Б","8 Б");
INSERT INTO class VALUES ("0","8 В","8 В");
INSERT INTO class VALUES ("0","9 А","9 А");
INSERT INTO class VALUES ("0","9 Б","9 Б");
INSERT INTO class VALUES ("0","9 В","9 В");
INSERT INTO class VALUES ("0","10 Технологический профиль","10 ТП");
INSERT INTO class VALUES ("0","10 Универсальный профиль","10 УП");
INSERT INTO class VALUES ("0","11 Технический профиль","11 ТП");
INSERT INTO class VALUES ("0","11 Универсальный профиль","11 УП");
INSERT INTO class VALUES ("0","Подготовительная группа","ПГ");
--
INSERT INTO teacher VALUES ("0","Гаврюшина","Любовь","Сергеевна","Гаврюшина ЛС");
INSERT INTO teacher VALUES ("0","Азарова","Светлана","Евгеньевна","Азарова СВ");
INSERT INTO teacher VALUES ("0","Андреанова","Людмила","Михайлова","Андреанова ЛМ");
INSERT INTO teacher VALUES ("0","Аникина","Ирина","Юрьевна","Аникина ИЮ");
INSERT INTO teacher VALUES ("0","Белякова","Оксана","Игоревна","Белякова ОИ");
INSERT INTO teacher VALUES ("0","Валяева","Екатерина","Валентиновна","Валяева ЕВ");
INSERT INTO teacher VALUES ("0","Васильева","Маргарита","Юрьевна","Васильева МЮ");
INSERT INTO teacher VALUES ("0","Волкова","Зинаида","Петровна","Волкова ЗП");
INSERT INTO teacher VALUES ("0","Еременко","Анна","Михайлова","Еременко АМ");
INSERT INTO teacher VALUES ("0","Журавлева","Надежда","Васильевна","Журавлева НВ");
INSERT INTO teacher VALUES ("0","Зыкова","Ольга","Вячеславовна","Зыкова ОВ");
INSERT INTO teacher VALUES ("0","Иванов","Александр","Васильевич","Иванов АВ");
INSERT INTO teacher VALUES ("0","Иванов","Константин","Евгеньевич","Иванов КЕ");
INSERT INTO teacher VALUES ("0","Иванова","Наталья","Алексеевна","Иванова НА");
INSERT INTO teacher VALUES ("0","Козачок","Лариса","Викторовна","Козачок ЛВ");
INSERT INTO teacher VALUES ("0","Козлова","Юлия","Валерьевна","Козлова ЮВ");
INSERT INTO teacher VALUES ("0","Колгина","Анастасия","Алексеевна","Колгина АА");
INSERT INTO teacher VALUES ("0","Костина","Наталья","Зусмановна","Костина НЗ");
INSERT INTO teacher VALUES ("0","Круглов","Александр","Александрович","Круглов АА");
INSERT INTO teacher VALUES ("0","Крымская","Елена","Эриковна","Крымская ЕЭ");
INSERT INTO teacher VALUES ("0","Кузнецов","Никита","Сергеевич","Кузнецов НС");
INSERT INTO teacher VALUES ("0","Кузнецова","Лариса","Алексеевна","Кузнецова ЛА");
INSERT INTO teacher VALUES ("0","Кулагин","Артур","Александрович","Кулагин АА");
INSERT INTO teacher VALUES ("0","Лянцева","Яна","Владимировна","Лянцева ЯВ");
INSERT INTO teacher VALUES ("0","Майорова","Татьяна","Барисова","Майорова ТБ");
INSERT INTO teacher VALUES ("0","Матросова","Елена","Владимировна","Матросова ЕВ");
INSERT INTO teacher VALUES ("0","Никитина","Ирина","Юрьевна","Никитина ИЮ");
INSERT INTO teacher VALUES ("0","Никитина","Светлана","Александровна","Никитина СА");
INSERT INTO teacher VALUES ("0","Николаева","Юлия","Николаевна","Николаева ЮН");
INSERT INTO teacher VALUES ("0","Обрядов","Александр","Владимирович","Обрядов АВ");
INSERT INTO teacher VALUES ("0","Овчинникова","Ирина","Васильевна","Овчинникова ИВ");
INSERT INTO teacher VALUES ("0","Павлова","Анеля","Васильевна","Павлова АВ");
INSERT INTO teacher VALUES ("0","Папина","Анна","Николаевна","Папина АН");
INSERT INTO teacher VALUES ("0","Петухова","Надежда","Юрьевна","Петухова НЮ");
INSERT INTO teacher VALUES ("0","Пикалев","Александр","Александрович","Пикалев АА");
INSERT INTO teacher VALUES ("0","Пикалева","Любовь","Юрьевна","Пикалева ЛЮ");
INSERT INTO teacher VALUES ("0","Подлесная","Елена","Михайловна","Подлесная ЕМ");
INSERT INTO teacher VALUES ("0","Попова","Елена","Юрьевна","Попова ЕЮ");
INSERT INTO teacher VALUES ("0","Савинова","Марина","Анатольевна","Савинова МА");
INSERT INTO teacher VALUES ("0","Смирнова","Галина","Анатольевна","Смирнова ГА");
INSERT INTO teacher VALUES ("0","Федорова","Ирина","Сергеевна","Федорова ИС");
INSERT INTO teacher VALUES ("0","Хроменкова","Екатерина","Игоревна","Хроменкова ЕИ");
INSERT INTO teacher VALUES ("0","Чеснокова","Марина","Сергеевна","Чеснокова МС");
INSERT INTO teacher VALUES ("0","Шамарова","Светлана","Геннадьевна","Шамарова СГ");
INSERT INTO teacher VALUES ("0","Янковская","Татьяна","Викторовна","Янковская ТВ");
--
INSERT INTO lesson VALUES ("0","1","1","1","1","1","1","1");
INSERT INTO lesson VALUES ("0","1","1","2","2","2","1","1");
INSERT INTO lesson VALUES ("0","1","1","3","3","3","1","1");
INSERT INTO lesson VALUES ("0","1","1","4","4","4","1","1");
--
