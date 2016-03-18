create table University (
	id Integer primary key,
	name VarChar
);

create table Host (
	-- For each archived year, specifies the hosting university.

	year Integer primary key,
	university Integer not null,

	constraint host__fk_university
		foreign key (university)
		references University(id)
		on delete cascade
		on update restrict
);

create table Competition (
	id Integer primary key,
	year Integer not null,
	name_en VarChar,
	name_fr VarChar,
	weight Double not null
		-- Competition weight out of 100
);

create table Team (
	id Integer primary key,
	year Integer not null,
		-- The year the team competed / will compete.
	university Integer not null,
	team_number Integer not null,
		-- Is-it the first or the second team of the specified university to
		-- register for the specified edition?
		-- `in (1, 2)`
	name VarChar,

	constraint team__fk_university
		foreign key (university)
		references University(id)
		on delete cascade
		on update restrict,
	constraint team__un_university_number
		unique (year, university, team_number)
);

create table Score (
	id Integer primary key,
	competiton Integer not null,
	team Integer not null,
	score Double not null default 0,
		-- Score out of 100

	constraint score__fk_competition
		foreign key (competition)
		references Competition(id)
		on delete cascade
		on update restrict,
	constraint score__fk_team
		foreign key (team)
		references Team(id)
		on delete cascade
		on update restrict,
	constraint score__un_competiton_team
		unique (competition, team)
);
