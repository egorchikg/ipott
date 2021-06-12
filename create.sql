--
--mysql
--
DROP TABLE IF EXISTS lesson;
DROP TABLE IF EXISTS class;
DROP TABLE IF EXISTS teacher;
DROP TABLE IF EXISTS interval;
DROP TABLE IF EXISTS weekday;
DROP TABLE IF EXISTS subject;
DROP TABLE IF EXISTS cabinet;
DROP TABLE IF EXISTS day;
--
--name = yyyy.mm.dd - 2018.05.25
--
CREATE TABLE day (
  id INT(11) NOT NULL AUTO_INCREMENT,
  name DATE,
  PRIMARY KEY (id)
)
CREATE TABLE cabinet (
  id INT(11) NOT NULL AUTO_INCREMENT,
  name VARCHAR(256),
  short_name VARCHAR(3),
  PRIMARY KEY (id)
)
CREATE TABLE subject (
  id INT(11) NOT NULL AUTO_INCREMENT,
  name VARCHAR(256),
  short_name VARCHAR(10),
  PRIMARY KEY (id)
)
CREATE TABLE weekday (
  id INT(11),
  name VARCHAR(256),
  short_name VARCHAR(2),
  n INT(11),
  PRIMARY KEY (id)
)
--
--start_time = hh:mi - 3:21
--
CREATE TABLE interval (
  id INT(11),
  n INT(11),
  start_time TIME,
  end_time TIME,
  PRIMARY KEY (id)
)
CREATE TABLE teacher (
  id INT(11),
  name VARCHAR(256),
  surname VARCHAR(256),
  patronymic VARCHAR(256),
  short_full_name VARCHAR(20),
  PRIMARY KEY (id)
)
CREATE TABLE class (
  id INT(11),
  name VARCHAR(256),
  short_name VARCHAR(35),
  PRIMARY KEY (id)
)
CREATE TABLE lesson (
  id INT(11),
  day_id INT(11),
  weekday_id INT(11),
  interval_id INT(11),
  subject_id INT(11),
  cabinet_id INT(11),
  teacher_id INT(11),
  class_id INT(11),
  --
  PRIMARY KEY (id),
  --
  KEY fk_lesson_day day_id,
  KEY fk_lesson_weekday weekday_id,
  KEY fk_lesson_interval interval_id,
  KEY fk_lesson_subject subject_id,
  KEY fk_lesson_cabinet cabinet_id,
  KEY fk_lesson_teacher teacher_id,
  KEY fk_lesson_class class_id,
  --
  CONSTRAINT fk_lesson_day
      FOREIGN KEY (day_id)
      REFERENCES day (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE,
  CONSTRAINT fk_lesson_weekday
      FOREIGN KEY (weekday_id)
      REFERENCES weekday (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE,
  CONSTRAINT fk_lesson_interval
      FOREIGN KEY (interval_id)
      REFERENCES interval (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE,
  CONSTRAINT fk_lesson_subject
      FOREIGN KEY (subject_id)
      REFERENCES subject (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE,
  CONSTRAINT fk_lesson_cabinet
      FOREIGN KEY (cabinet_id)
      REFERENCES cabinet (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE,
  CONSTRAINT fk_lesson_teacher
      FOREIGN KEY (teacher_id)
      REFERENCES teacher (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE,
  CONSTRAINT fk_lesson_class
      FOREIGN KEY (class_id)
      REFERENCES class (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
)
