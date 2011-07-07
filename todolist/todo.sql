# sqllite3
CREATE TABLE [todo] (id integer PRIMARY KEY AUTOINCREMENT,title text)

# postgresql-9.0
CREATE TABLE todo
(
  title text,
  id serial NOT NULL,
  CONSTRAINT id PRIMARY KEY (id)
)