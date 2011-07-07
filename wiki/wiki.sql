CREATE TABLE pages
(
  id serial NOT NULL,
  url text,
  title text,
  "content" text,
  CONSTRAINT pages_pkey PRIMARY KEY (id)
)

