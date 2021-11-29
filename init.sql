DROP USER IF EXISTS 'ipott_user'@'localhost';
--
DROP DATABASE IF EXISTS ipott_db;
--
FLUSH PRIVILEGES;
--
CREATE USER 'ipott_user'@'localhost'
IDENTIFIED BY 'ipott_pass';
--
CREATE DATABASE ipott_db;
--
GRANT ALL PRIVILEGES ON ipott_db.*
TO 'ipott_user'@'localhost';
--
USE ipott_db;
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
INSERT INTO day VALUES ("0","2021.11.24");
INSERT INTO day VALUES ("0","2021.11.25");
INSERT INTO day VALUES ("0","2021.11.26");
INSERT INTO day VALUES ("0","2021.11.27");
INSERT INTO day VALUES ("0","2021.11.28");
INSERT INTO day VALUES ("0","2021.11.29");
--
INSERT INTO cabinet VALUES ("0","Актовый зал","акт.");
INSERT INTO cabinet VALUES ("0","Учительская","уч.");
INSERT INTO cabinet VALUES ("0","Улица","ул.");
INSERT INTO cabinet VALUES ("0","Столярная мастерская","мас.");
INSERT INTO cabinet VALUES ("0","Спортивный зал","с.з.");
INSERT INTO cabinet VALUES ("0","Кабинет № 1","1к.");
INSERT INTO cabinet VALUES ("0","Кабинет № 2","2к.");
INSERT INTO cabinet VALUES ("0","Кабинет № 3","3к.");
INSERT INTO cabinet VALUES ("0","Кабинет № 4","4к.");
INSERT INTO cabinet VALUES ("0","Кабинет № 5","5к.");
INSERT INTO cabinet VALUES ("0","Кабинет № 6","6к.");
INSERT INTO cabinet VALUES ("0","Кабинет № 7","7к.");
INSERT INTO cabinet VALUES ("0","Кабинет № 8","8к.");
INSERT INTO cabinet VALUES ("0","Кабинет № 9","9к.");
INSERT INTO cabinet VALUES ("0","Кабинет № 10","10к.");
INSERT INTO cabinet VALUES ("0","Кабинет № 11","11к.");
INSERT INTO cabinet VALUES ("0","Кабинет № 12","12к.");
INSERT INTO cabinet VALUES ("0","Кабинет № 13","13к.");
INSERT INTO cabinet VALUES ("0","Кабинет № 14","14к.");
INSERT INTO cabinet VALUES ("0","Кабинет № 15","15к.");
INSERT INTO cabinet VALUES ("0","Кабинет № 16","16к.");
INSERT INTO cabinet VALUES ("0","Кабинет № 17","17к.");
INSERT INTO cabinet VALUES ("0","Кабинет № 18","18к.");
INSERT INTO cabinet VALUES ("0","Кабинет № 19","19к.");
INSERT INTO cabinet VALUES ("0","Кабинет № 20","20к.");
INSERT INTO cabinet VALUES ("0","Кабинет № 21","21к.");
INSERT INTO cabinet VALUES ("0","Кабинет № 22","22к.");
INSERT INTO cabinet VALUES ("0","Кабинет № 23","23к.");
INSERT INTO cabinet VALUES ("0","Кабинет № 24","24к.");
INSERT INTO cabinet VALUES ("0","Кабинет № 25","25к.");
INSERT INTO cabinet VALUES ("0","Кабинет № 26","26к.");
INSERT INTO cabinet VALUES ("0","Кабинет № 27","27к.");
--
INSERT INTO subject VALUES ("0","Физкультура","Физ-ра");
INSERT INTO subject VALUES ("0","Литература","Литература");
INSERT INTO subject VALUES ("0","Технология","Технология");
INSERT INTO subject VALUES ("0","Русский язык","Рус.яз.");
INSERT INTO subject VALUES ("0","Математика","Матем.");
INSERT INTO subject VALUES ("0","Математика электив","Матем.э.");
INSERT INTO subject VALUES ("0","ИЗО","ИЗО");
INSERT INTO subject VALUES ("0","Музыка","Музыка");
INSERT INTO subject VALUES ("0","Немецкий язык","Нем.яз.");
INSERT INTO subject VALUES ("0","Английский язык","Англ.яз.");
INSERT INTO subject VALUES ("0","Английский язык 1","Англ.яз.1");
INSERT INTO subject VALUES ("0","Английский язык 2","Англ.яз.2");
INSERT INTO subject VALUES ("0","Биология","Биол.");
INSERT INTO subject VALUES ("0","Биология элективБиол.э.");
INSERT INTO subject VALUES ("0","Химия","Химия");
INSERT INTO subject VALUES ("0","Физика","Физика");
INSERT INTO subject VALUES ("0","География","Геогр.");
INSERT INTO subject VALUES ("0","ОБЖ","ОБЖ");
INSERT INTO subject VALUES ("0","История","Ист.");
INSERT INTO subject VALUES ("0","История электив","Ист.э.");
INSERT INTO subject VALUES ("0","Астрономия","Астр.");
INSERT INTO subject VALUES ("0","Обществознание","Общ.");
INSERT INTO subject VALUES ("0","Экономика","Экономика");
INSERT INTO subject VALUES ("0","Право","Право");
INSERT INTO subject VALUES ("0","-","-");
INSERT INTO subject VALUES ("0","Классный час","Кл.ч.");
INSERT INTO subject VALUES ("0","Родной язык","Родн.яз.");
INSERT INTO subject VALUES ("0","Родная литература","Родн.лит.");
INSERT INTO subject VALUES ("0","Информатика","Инф.");
INSERT INTO subject VALUES ("0","Информатика 1","Инф.1");
INSERT INTO subject VALUES ("0","Информатика 2","Инф.2");
INSERT INTO subject VALUES ("0","Алгебра","Алгебра");
INSERT INTO subject VALUES ("0","Геометрия","Геом.");
INSERT INTO subject VALUES ("0","Индивидуальный проект","Инд.пр.");
--
INSERT INTO lapse VALUES ("0","0","08:00","08:30");
INSERT INTO lapse VALUES ("0","1","08:30","09:15");
INSERT INTO lapse VALUES ("0","2","09:25","10:10");
INSERT INTO lapse VALUES ("0","3","10:30","11:15");
INSERT INTO lapse VALUES ("0","4","11:35","12:20");
INSERT INTO lapse VALUES ("0","5","12:30","13:15");
INSERT INTO lapse VALUES ("0","6","13:25","14:10");
INSERT INTO lapse VALUES ("0","7","14:15","15:00");
--
INSERT INTO class VALUES ("0","5 А","5а");
INSERT INTO class VALUES ("0","5 Б","5б");
INSERT INTO class VALUES ("0","6 А","6а");
INSERT INTO class VALUES ("0","6 Б","6б");
INSERT INTO class VALUES ("0","7 А","7а");
INSERT INTO class VALUES ("0","7 Б","7б");
INSERT INTO class VALUES ("0","8 А","8а");
INSERT INTO class VALUES ("0","8 Б","8б");
INSERT INTO class VALUES ("0","9 А","9а");
INSERT INTO class VALUES ("0","9 Б","9б");
INSERT INTO class VALUES ("0","9 В","9в");
INSERT INTO class VALUES ("0","10","10");
INSERT INTO class VALUES ("0","11","11");
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
INSERT INTO lesson VALUES ("0","1","1","1","1","1","1");
--
