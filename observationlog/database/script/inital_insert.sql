INSERT INTO tblobservation (obs_id,obs_equ_fk,obs_loc_fk,obs_object,obs_ra,obs_dec,obs_typ_fk,obs_con_fk,obs_observer,obs_datetime,obs_condition_txt,obs_see_fk,obs_description,obs_magnification,obs_fov, obs_image)
	VALUES (1,NULL,1,'M 13',251.108,36.461,1,NULL,'Marcus Vasi','2022-03-02 22:15:00','The quick brown fox jumps over the lazy dog',NULL,'Bla Bla Blubb',120,NULL,NULL);
	
INSERT INTO tbllocation (loc_id,loc_name,loc_lat,loc_lon)
    VALUES (1,'Erkrath-Hochdahl',51.210805,6.967999);