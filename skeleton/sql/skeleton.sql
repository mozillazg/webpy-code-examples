CREATE TABLE items
(
  id serial NOT NULL,
  author_id integer,
  body text,
  created time without time zone DEFAULT timezone('utc'::text, now()),
  CONSTRAINT items_pkey PRIMARY KEY (id)
)

