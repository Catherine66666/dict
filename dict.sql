create table if not exists dictionary (
  id serial,
  word varchar(50),
  translation varchar(50)
);

insert into dictionary
  (word, translation)
values
  ('sun', 'sol'),
  ('moon', 'måne'),
  ('star', 'stjärna'),
  ('planet', 'planet'),
  ('observe', 'observera'),
  ('study', 'undersöka'),
  ('investigate', 'utforska')
;

