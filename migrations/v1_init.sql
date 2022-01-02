CREATE TABLE one (
  id SERIAL NOT NULL PRIMARY KEY,
  val TEXT NOT NULL;
);

CREATE TABLE two (
  id SERIAL NOT NULL PRIMARY KEY,
  one_id INT NOT NULL,
  val TEXT NOT NULL;
)

CREATE TABLE three (
  id SERIAL NOT NULL PRIMARY KEY,
  one_id INT NOT NULL REFERENCES one (id),
  two_id INT NOT NULL REFERENCES two (id),
  val TEXT NOT NULL;
)

CREATE VIEW myview AS
SELECT * FROM one;