CREATE VIEW OBSERVATIONS AS
    SELECT tblobservation.obs_equ_fk,
           tbllocation.loc_name,
           tblobservation.obs_object,
           tblobservation.obs_ra,
           tblobservation.obs_dec,
           tblobservation.obs_typ_fk,
           tblobservation.obs_con_fk,
           tblobservation.obs_observer,
           tblobservation.obs_datetime,
           tblobservation.obs_condition_txt
      FROM tblobservation,
           tbllocation
     WHERE tblobservation.obs_loc_fk = tbllocation.loc_id;