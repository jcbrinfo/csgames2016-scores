create table competitions (
	compID Integer primary key,
	compName_en VarChar(255),
	compName_fr VarChar(255),
	compWeight Double not null default 0,
		-- Competition weight out of 100
	compResultsLink VarChar(250)
);

create table delegations (
	delegID Integer primary key,
	delegUniversity VarChar(200) not null default '',
	delegAddress1 VarChar(100) not null default '',
	delegAddress2 VarChar(100),
	delegAddress3 VarChar(100),
	delegCity VarChar(100) not null default '',
	delegProv VarChar(50),
	delegCountry VarChar(20) not null default 'Canada',
		-- in ('Canada','United States','Other')
	delegPostal VarChar(15),
	delegUsername VarChar(30) not null default '',
	delegPassword VarChar(64) not null default '',
	regIsCancelled Integer not null default 0,
	regDate VarChar(50) not null default 'unknown',
	regCancelDate VarChar(50),
	hotelDetails VarChar,
	extraHotelRooms Integer not null default 0,
	extraHotelNights Integer not null default 0,
	delegAlias VarChar(60) not null default '',
	delegLanguage Char(2) not null default 'en',
		-- in ('fr','en')
	didFlashOut Integer not null default 0,
	flashOutFile VarChar(255),
	adminNotes VarChar,
	excludeFromOverallResults Integer not null,
	delegSite VarChar(255)
);

create table compscores (
	compID Integer not null,
	delegID Integer not null,
	teamScore Double not null default 0,
		-- Score out of 100

	constraint compscores__pk
		primary key (compID,delegID),
	constraint compscores__fk_compID
		foreign key (compID)
		references competitions(compID)
		on delete cascade
		on update restrict,
	constraint compscores__fk_delegID
		foreign key (delegID)
		references delegatinos(delegID)
		on delete cascade
		on update restrict
);
