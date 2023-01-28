DROP TABLE IF EXISTS tbllocation;
CREATE TABLE tbllocation(
	loc_id				INT PRIMARY KEY	NOT NULL,
	loc_name			VARCHAR(50)		NOT NULL,
	loc_lat				DECIMAL(8,6)	NOT NULL,
	loc_lon				DECIMAL(9,6)	NOT NULL
);
DROP TABLE IF EXISTS tbltelescope;
CREATE TABLE tbltelescope(
	tel_id				INT PRIMARY KEY	NOT NULL,
	tel_manufacturer	VARCHAR(50)		NOT NULL,
	tel_type			VARCHAR(50)		NOT NULL,
	tel_aperture		INT				NOT NULL,
	tel_foc_length		INT				NOT NULL
);
DROP TABLE IF EXISTS tblbinocular(
	bin_id				INT PRIMARY KEY NOT NULL,
	bin_manufacturer	VARCHAR(50)		NOT NULL,
	bin_magnification	INT				NOT NULL,
	bin_aperture		INT				NOT NULL,
	bin_fov				INT				NOT NULL
);
